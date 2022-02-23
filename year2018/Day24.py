from utils import load_text_blocks
from copy import deepcopy
import re

INPUT_FILE = "./year2018/data/day24.txt"


class Group:
    def __init__(self, name, units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities):
        self.name = name
        self.units = units
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

    def effective_power(self):
        return self.units * self.attack_damage

    def damage(self, target):
        if self.attack_type in target.immunities:
            return 0
        elif self.attack_type in target.weaknesses:
            return 2 * self.effective_power()
        else:
            return self.effective_power()


def load_data(filename):
    immune_system, infection = [], []
    for text_block in load_text_blocks(filename):
        who, name, grp = [], "", 1
        for line in text_block:
            if line == "Immune System:":
                who, name, grp = immune_system, "immune system group ", 1
            elif line == "Infection:":
                who, name, grp = infection, "infection group ", 1
            else:
                p = re.compile(r"(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (.*) " +
                               r"damage at initiative (\d+)").match(line)
                units = int(p.group(1))
                hit_points = int(p.group(2))
                weaknesses, immunities = set(), set()
                tmp = p.group(3)
                if len(tmp) > 0:
                    tmp = tmp.strip().replace("(", "").replace(")", "")
                    for x in tmp.split("; "):
                        if x.startswith("immune to "):
                            immunities = set(list(x[10:].split(", ")))
                        elif x.startswith("weak to "):
                            weaknesses = set(list(x[8:].split(", ")))
                attack_damage = int(p.group(4))
                attack_type = p.group(5)
                initiative = int(p.group(6))
                who += [Group(name + str(grp), units, hit_points, attack_damage, attack_type, initiative, weaknesses,
                              immunities)]
                grp += 1
    return immune_system, infection


def select_target(attacker, targets):
    if len(targets) == 0:
        return None
    targets_sorted = sorted(targets, key=lambda x: (-attacker.damage(x), -x.effective_power(), -x.initiative))
    if attacker.damage(targets_sorted[0]) == 0:
        return None
    return targets_sorted[0]


def select_targets(attackers, targets):
    selection = {}
    targets_remaining = targets.copy()
    for attacker in sorted(attackers, key=lambda x: (-x.effective_power(), -x.initiative)):
        target = select_target(attacker, targets_remaining)
        if target is not None:
            selection[attacker] = target
            targets_remaining.remove(target)
    return selection


def combat(immune_system, infection, boost=0):
    for x in immune_system:
        x.attack_damage += boost
    while True:
        total_loss = 0
        targets = {**select_targets(infection, immune_system), **select_targets(immune_system, infection)}
        for attacker in sorted(immune_system + infection, key=lambda x: -x.initiative):
            if attacker.units > 0 and attacker in targets:
                target = targets[attacker]
                unit_loss = min(target.units, attacker.damage(target) // target.hit_points)
                target.units -= unit_loss
                total_loss += unit_loss
        immune_system, infection = [x for x in immune_system if x.units > 0], [x for x in infection if x.units > 0]
        if total_loss == 0:
            return "draw", 0
        elif len(immune_system) == 0:
            return "infection", sum([x.units for x in infection])
        elif len(infection) == 0:
            return "immune system", sum([x.units for x in immune_system])


immune_system, infection = load_data(INPUT_FILE)

_, units = combat(deepcopy(immune_system), deepcopy(infection))
print("part 1:", units)

winner, boost = None, 0
while winner != "immune system":
    (winner, units), boost = combat(deepcopy(immune_system), deepcopy(infection), boost), boost + 1
print("part 2:", units)

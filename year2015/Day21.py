import math
from itertools import combinations

file = open("./year2015/data/day21.txt", "r")
lines = [line.rstrip('\n') for line in file]

weapons = [("Dagger", 8, 4, 0),
           ("Shortsword", 10, 5, 0),
           ("Warhammer", 25, 6, 0),
           ("Longsword", 40, 7, 0),
           ("Greataxe", 74, 8, 0)]

armor = [("Leather", 13, 0, 1),
         ("Chainmail", 31, 0, 2),
         ("Splintmail", 53, 0, 3),
         ("Bandedmail", 75, 0, 4),
         ("Platemail", 102, 0, 5)]

rings = [("Damage +1", 25, 1, 0),
         ("Damage +2", 50, 2, 0),
         ("Damage +3", 100, 3, 0),
         ("Defense +1", 20, 0, 1),
         ("Defense +2", 40, 0, 2),
         ("Defense +3", 80, 0, 3)]


def play(player_1, player_2):
    hit_points_1, damage_1, armor_1 = player_1
    hit_points_2, damage_2, armor_2 = player_2
    damage = max(damage_1 - armor_2, 1)
    hit_points_2 -= damage
    if hit_points_2 <= 0:
        return True
    else:
        return not play((hit_points_2, damage_2, armor_2), (hit_points_1, damage_1, armor_1))


def build_player(weapon_choice, armor_choice, ring_choice):
    hit_points, damage, armor, cost = 100, 0, 0, 0
    for w in weapon_choice:
        cost += w[1]
        damage += w[2]
    for a in armor_choice:
        cost += a[1]
        armor += a[3]
    for r in ring_choice:
        cost += r[1]
        damage += r[2]
        armor += r[3]
    return (hit_points, damage, armor), cost


boss_hit_points = int(lines[0].split(" ")[2])
boss_damage = int(lines[1].split(" ")[1])
boss_armor = int(lines[2].split(" ")[1])

weapon_choices = []
for c in combinations(weapons, 1):
    weapon_choices.append(list(c))
armor_choices = []
for i in range(2):
    for c in combinations(armor, i):
        armor_choices.append(list(c))
ring_choices = []
for i in range(3):
    for c in combinations(rings, i):
        ring_choices.append(list(c))

best_cost, worst_cost = math.inf, 0
for w in weapon_choices:
    for a in armor_choices:
        for r in ring_choices:
            player, cost = build_player(w, a, r)
            boss = (boss_hit_points, boss_damage, boss_armor)
            if play(player, boss):
                best_cost = min(best_cost, cost)
            else:
                worst_cost = max(worst_cost, cost)
print(best_cost)
print(worst_cost)

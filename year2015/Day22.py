from collections import namedtuple
import functools
import math
from datetime import datetime

Player = namedtuple("Player", ["hit_points", "armor", "mana"])
Boss = namedtuple("Boss", ["hit_points", "damage"])
Effects = namedtuple("Effects", ["shield", "poison", "recharge"])

file = open("./year2015/data/day22.txt", "r")
lines = [line.rstrip('\n') for line in file]


@functools.lru_cache(maxsize=None)
def play(player, boss, effects, mana_used, is_turn_player, is_hard):
    player_tmp = player._asdict()
    boss_tmp = boss._asdict()
    effects_tmp = effects._asdict()

    if is_turn_player and is_hard:
        player_tmp["hit_points"] -= 1
        if player_tmp["hit_points"] <= 0:
            return math.inf

    # shield effect
    if effects_tmp["shield"] == 0:
        player_tmp["armor"] = 0
    else:
        effects_tmp["shield"] -= 1

    # poison effect
    if effects_tmp["poison"] > 0:
        boss_tmp["hit_points"] -= 3
        if boss_tmp["hit_points"] <= 0:
            return mana_used
        effects_tmp["poison"] -= 1

    # recharge effect
    if effects_tmp["recharge"] > 0:
        player_tmp["mana"] += 101
        effects_tmp["recharge"] -= 1

    if is_turn_player:

        best_mana_used = math.inf

        # cast magic missile
        if player_tmp["mana"] >= 53:
            mana_used_next = mana_used + 53
            player_next = player_tmp.copy()
            boss_next = boss_tmp.copy()
            effects_next = effects_tmp.copy()
            player_next["mana"] -= 53
            boss_next["hit_points"] -= 4
            if boss_next["hit_points"] <= 0:
                return mana_used_next
            res = play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, False,
                       is_hard)
            best_mana_used = min(best_mana_used, res)

        # cast drain
        if player_tmp["mana"] >= 73:
            mana_used_next = mana_used + 73
            player_next = player_tmp.copy()
            boss_next = boss_tmp.copy()
            effects_next = effects_tmp.copy()
            player_next["mana"] -= 73
            player_next["hit_points"] += 2
            boss_next["hit_points"] -= 2
            if boss_next["hit_points"] <= 0:
                return mana_used_next
            res = play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, False,
                       is_hard)
            best_mana_used = min(best_mana_used, res)

        # cast shield
        if player_tmp["mana"] >= 113 and effects_tmp["shield"] == 0:
            mana_used_next = mana_used + 113
            player_next = player_tmp.copy()
            boss_next = boss_tmp.copy()
            effects_next = effects_tmp.copy()
            player_next["mana"] -= 113
            player_next["armor"] += 7
            effects_next["shield"] = 6
            res = play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, False,
                       is_hard)
            best_mana_used = min(best_mana_used, res)

        # cast poison
        if player_tmp["mana"] >= 173 and effects_tmp["poison"] == 0:
            mana_used_next = mana_used + 173
            player_next = player_tmp.copy()
            boss_next = boss_tmp.copy()
            effects_next = effects_tmp.copy()
            player_next["mana"] -= 173
            effects_next["poison"] = 6
            res = play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, False,
                       is_hard)
            best_mana_used = min(best_mana_used, res)

        # cast recharge
        if player_tmp["mana"] >= 229 and effects_tmp["recharge"] == 0:
            mana_used_next = mana_used + 229
            player_next = player_tmp.copy()
            boss_next = boss_tmp.copy()
            effects_next = effects_tmp.copy()
            player_next["mana"] -= 229
            effects_next["recharge"] = 5
            res = play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, False,
                       is_hard)
            best_mana_used = min(best_mana_used, res)

        return best_mana_used

    else:
        mana_used_next = mana_used
        player_next = player_tmp.copy()
        boss_next = boss_tmp.copy()
        effects_next = effects_tmp.copy()
        player_next["hit_points"] -= max(boss_next["damage"] - player_next["armor"], 1)
        if player_next["hit_points"] <= 0:
            return math.inf
        else:
            return play(Player(**player_next), Boss(**boss_next), Effects(**effects_next), mana_used_next, True,
                        is_hard)


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

player_start = Player(50, 0, 500)
boss_start = Boss(int(lines[0].split(" ")[2]), int(lines[1].split(" ")[1]))
effects_start = Effects(0, 0, 0)

print("part1 :", play(player_start, boss_start, effects_start, 0, True, False))
print("part2 :", play(player_start, boss_start, effects_start, 0, True, True))

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

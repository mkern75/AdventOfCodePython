from collections import Counter

file = open("./year2021/data/day21.txt", "r")
lines = [line.rstrip('\n') for line in file]


def play1(pos1, scr1, pos2, scr2, die_rolls):
    rolls = die_rolls % 100 + 1 + (die_rolls + 1) % 100 + 1 + (die_rolls + 2) % 100 + 1
    die_rolls += 3
    pos1 = (pos1 - 1 + rolls) % 10 + 1
    scr1 += pos1
    if scr1 >= 1000:
        return scr2 * die_rolls
    else:
        return play1(pos2, scr2, pos1, scr1, die_rolls)


def play2(pos1, scr1, pos2, scr2, idx_player, freq, wins, counter_dice):
    for sum_dice in counter_dice.keys():
        npos1 = (pos1 - 1 + sum_dice) % 10 + 1
        nscr1 = scr1 + npos1
        nfreq = freq * counter_dice[sum_dice]
        if nscr1 >= 21:
            wins[idx_player] += nfreq
        else:
            play2(pos2, scr2, npos1, nscr1, 1 - idx_player, nfreq, wins, counter_dice)
    return max(wins)


start_pos = [int(line[28:]) for line in lines]

ans1 = play1(start_pos[0], 0, start_pos[1], 0, 0)
print("part 1:", ans1)

counter_dice = Counter({3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1})
ans2 = play2(start_pos[0], 0, start_pos[1], 0, 0, 1, [0, 0], counter_dice)
print("part 2:", ans2)

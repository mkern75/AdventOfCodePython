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


def play2(pos1, scr1, pos2, scr2, DP):
    if scr1 >= 21:
        return 1, 0
    elif scr2 >= 21:
        return 0, 1
    elif (pos1, scr1, pos2, scr2) in DP:
        return DP[(pos1, scr1, pos2, scr2)]
    wins = (0, 0)
    for r1 in [1, 2, 3]:
        for r2 in [1, 2, 3]:
            for r3 in [1, 2, 3]:
                npos1 = (pos1 - 1 + r1 + r2 + r3) % 10 + 1
                nscr1 = scr1 + npos1
                w2, w1 = play2(pos2, scr2, npos1, nscr1, DP)
                wins = (wins[0] + w1, wins[1] + w2)
    DP[(pos1, scr1, pos2, scr2)] = wins
    return wins


start_pos = [int(line[28:]) for line in lines]
ans1 = play1(start_pos[0], 0, start_pos[1], 0, 0)
print("part 1:", ans1)
ans2 = max(play2(start_pos[0], 0, start_pos[1], 0, {}))
print("part 2:", ans2)

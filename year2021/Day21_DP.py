import functools

file = open("./year2021/data/day21.txt", "r")
lines = [line.rstrip('\n') for line in file]

QUANTUM_DICE_ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def play1(player1, score1, player2, score2, die_rolls):
    rolls = die_rolls % 100 + 1 + (die_rolls + 1) % 100 + 1 + (die_rolls + 2) % 100 + 1
    die_rolls += 3
    player1 = (player1 - 1 + rolls) % 10 + 1
    score1 += player1
    if score1 >= 1000:
        return score2 * die_rolls
    else:
        return play1(player2, score2, player1, score1, die_rolls)


@functools.lru_cache(maxsize=None)  # Dynamic Programming with a single line of code!
def play2(player1, score1, player2, score2):
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1
    wins1, wins2 = 0, 0
    for rolls, freq in QUANTUM_DICE_ROLLS.items():
        player1_new = (player1 - 1 + rolls) % 10 + 1
        score1_new = score1 + player1_new
        w2, w1 = play2(player2, score2, player1_new, score1_new)
        wins1 += w1 * freq
        wins2 += w2 * freq
    return wins1, wins2


start1, start2 = [int(line[28:]) for line in lines]
ans1 = play1(start1, 0, start2, 0, 0)
print("part 1:", ans1)
ans2 = max(play2(start1, 0, start2, 0))
print("part 2:", ans2)

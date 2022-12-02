INPUT_FILE = "./year2022/data/day02.txt"

# r=rock, p=paper, s=scissors
CHOICE = {"A": "r", "B": "p", "C": "s", "X": "r", "Y": "p", "Z": "s"}

# w=win, d=draw, l=loss
OUTCOME = {("r", "r"): "d", ("r", "p"): "w", ("r", "s"): "l",
           ("p", "r"): "l", ("p", "p"): "d", ("p", "s"): "w",
           ("s", "r"): "w", ("s", "p"): "l", ("s", "s"): "d",
           "X": "l", "Y": "d", "Z": "w"}

# scores
CHOICE_SCORE = {"r": 1, "p": 2, "s": 3}
OUTCOME_SCORE = {"w": 6, "d": 3, "l": 0}

ans1, ans2 = 0, 0
for line in [line.rstrip('\n') for line in open(INPUT_FILE, "r")]:
    elf, you = line.split()
    # part 1
    choice_elf = CHOICE[elf]
    choice_you = CHOICE[you]
    outcome = OUTCOME[(choice_elf, choice_you)]
    ans1 += OUTCOME_SCORE[outcome] + CHOICE_SCORE[choice_you]
    # part 2
    choice_elf = CHOICE[elf]
    outcome = OUTCOME[you]
    choice_you = next(x for x in OUTCOME if x[0] == choice_elf and OUTCOME[x] == outcome)[1]
    ans2 += OUTCOME_SCORE[outcome] + CHOICE_SCORE[choice_you]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

INPUT_FILE = "./year2020/data/day06.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

questions, yes = set(), [0]
for line in data:
    if line == "":
        questions = set()
        yes += [0]
    else:
        questions |= set(line)
        yes[-1] = len(questions)
print(f"part 1: {sum(yes)}")

questions, yes = set("abcdefghijklmnopqrstuvwxyz"), [0]
for line in data:
    if line == "":
        questions = set("abcdefghijklmnopqrstuvwxyz")
        yes += [0]
    else:
        questions &= set(line)
        yes[-1] = len(questions)
print(f"part 2: {sum(yes)}")

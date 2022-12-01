import utils

INPUT_FILE = "./year2022/data/day01.txt"
data = utils.load_lines(INPUT_FILE)

elves = [0]
for cal in data:
    if cal == "":
        elves += [0]
    else:
        elves[-1] += int(cal)

elves.sort(reverse=True)
ans1 = elves[0]
ans2 = sum(elves[:3])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

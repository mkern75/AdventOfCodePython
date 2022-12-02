INPUT_FILE = "./year2022/data/day01.txt"

elves = [0]
for cal in [line.rstrip('\n') for line in open(INPUT_FILE, "r")]:
    if cal == "":
        elves += [0]
    else:
        elves[-1] += int(cal)

elves.sort(reverse=True)
ans1 = elves[0]
ans2 = sum(elves[:3])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

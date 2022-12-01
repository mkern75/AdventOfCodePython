INPUT_FILE = "./year2022/data/day01.txt"

elves, elf = [], 0
for cal in [line.rstrip('\n') for line in open(INPUT_FILE, "r")]:
    if cal == "":
        elves += [elf]
        elf = 0
    else:
        elf += int(cal)
elves += [elf]

elves.sort(reverse=True)
ans1 = elves[0]
ans2 = sum(elves[:3])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

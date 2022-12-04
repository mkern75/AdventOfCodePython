INPUT_FILE = "./year2022/data/day04.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0
for line in data:
    a, b = line.split(",")
    elf1 = list(map(int, a.split("-")))
    elf2 = list(map(int, b.split("-")))
    if elf1[0] <= elf2[0] <= elf2[1] <= elf1[1] or elf2[0] <= elf1[0] <= elf1[1] <= elf2[1]:
        ans1 += 1
    if elf1[0] <= elf2[1] and elf1[1] >= elf2[0]:
        ans2 += 1

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

INPUT_FILE = "./year2022/data/day03.txt"
rucksacks = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
for rucksack in rucksacks:
    n = len(rucksack) // 2
    item, = set(rucksack[:n]) & set(rucksack[n:])
    ans1 += ord(item) + (1 - ord("a") if item.islower() else 27 - ord("A"))
print(f"part 1: {ans1}")

ans2 = 0
for i in range(0, len(rucksacks), 3):
    item, = set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
    ans2 += ord(item) + (1 - ord("a") if item.islower() else 27 - ord("A"))
print(f"part 2: {ans2}")

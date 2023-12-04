from collections import defaultdict

INPUT_FILE = "./year2023/data/day03.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
R, C = len(data), len(data[0])

ans1, ans2 = 0, 0

gears = defaultdict(list)
for r, line in enumerate(data):
    start = 0
    while True:
        start = next((i for i in range(start, C) if line[i].isdigit()), C)
        if start == C:
            break
        end = next((i for i in range(start, C) if not line[i].isdigit()), C) - 1
        num = int(line[start:end + 1])
        is_part = False
        for rn in range(r - 1, r + 2):
            for cn in range(start - 1, end + 2):
                if 0 <= rn < R and 0 <= cn < C:
                    if not data[rn][cn].isdigit() and data[rn][cn] != ".":
                        is_part = True
                    if data[rn][cn] == "*":
                        gears[rn, cn] += [num]
        if is_part:
            ans1 += num
        start = end + 1

ans2 = sum(nums[0] * nums[1] for nums in gears.values() if len(nums) == 2)

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

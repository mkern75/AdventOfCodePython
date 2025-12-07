from time import time
from collections import defaultdict, Counter

time_start = time()
INPUT_FILE = "./year2025/data/day07.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
grid = defaultdict(lambda: ".", {(r, c): v for r, row in enumerate(data) for c, v in enumerate(row)})

ans1 = 0
cnt = Counter({data[0].index("S"): 1})
for r in range(len(data) - 1):
    cnt_new = Counter()
    for c, v in cnt.items():
        if grid[r + 1, c] == "^":
            ans1 += 1
            cnt_new[c - 1] += v
            cnt_new[c + 1] += v
        else:
            cnt_new[c] += v
    cnt = cnt_new
ans2 = sum(cnt.values())

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

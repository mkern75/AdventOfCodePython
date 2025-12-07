from time import time
from collections import Counter

time_start = time()
INPUT_FILE = "./year2025/data/day07.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
n_rows, n_cols = len(grid), len(grid[0])

ans1 = 0
cnt = Counter({grid[0].index("S"): 1})
for r in range(n_rows - 1):
    cnt_new = Counter()
    for c, v in cnt.items():
        if grid[r + 1][c] == "^":
            ans1 += 1
            if 0 <= c - 1:
                cnt_new[c - 1] += v
            if c + 1 < n_cols:
                cnt_new[c + 1] += v
        else:
            cnt_new[c] += v
    cnt = cnt_new
ans2 = sum(cnt.values())

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

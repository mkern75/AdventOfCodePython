from time import time
import pyperclip
import re
from collections import defaultdict, Counter


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


def neighbours4(r, c, n_rows, n_cols):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= rn < n_rows and 0 <= cn < n_cols:
            yield rn, cn


def neighbours8(r, c, n_rows, n_cols):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
                   (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
        if 0 <= rn < n_rows and 0 <= cn < n_cols:
            yield rn, cn


time_start = time()
INPUT_FILE = "./year2025/data/day01test.txt"
# INPUT_FILE = "./year2025/data/day01.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
# R, C = len(data), len(data[0])
# blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]
# grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
# R, C = len(grid), len(grid[0])
# grid = defaultdict(lambda: ".", {(r, c): v for r, row in enumerate(data) for c, v in enumerate(row)})
ans1, ans2 = 0, 0

for line in data:
    pass

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
pyperclip.copy(str(ans1))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")
# pyperclip.copy(str(ans1))

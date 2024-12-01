from time import time

time_start = time()
# INPUT_FILE = "./year2024/data/day00test.txt"
INPUT_FILE = "./year2024/data/day00.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
# blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]
# grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
# R, C = len(grid), len(grid[0])

ans1, ans2 = 0, 0

for line in data:
    pass

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

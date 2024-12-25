from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day25.txt"
schematics = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]
R, C = len(schematics[0]), len(schematics[0][0])

locks, keys = [], []
for schematic in schematics:
    if schematic[0][0] == "#":
        locks.append(tuple(next(r for r in range(R - 1, -1, -1) if schematic[r][c] == "#") for c in range(C)))
    else:
        keys.append(tuple((R - 1 - next(r for r in range(R) if schematic[r][c] == "#")) for c in range(C)))

ans1 = 0
for key in keys:
    for lock in locks:
        if all(key[c] + lock[c] <= R - 2 for c in range(C)):
            ans1 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

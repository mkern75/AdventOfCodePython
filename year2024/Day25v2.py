from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day25.txt"
schematics = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]
R, C = len(schematics[0]), len(schematics[0][0])

locks, keys = [], []
for schematic in schematics:
    if schematic[0][0] == "#":
        locks += [schematic]
    else:
        keys += [schematic]


def fits(lock, key):
    for c in range(C):
        for r in range(R):
            if lock[r][c] == key[r][c] == "#":
                return 0
    return 1


ans1 = 0
for lock in locks:
    for key in keys:
        ans1 += fits(lock, key)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

from time import time
from functools import cache

time_start = time()

INPUT_FILE = "./year2024/data/day19.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

available_patterns = list(blocks[0][0].split(", "))


@cache
def count_ways(design):
    if not design:
        return 1
    return sum(count_ways(design[len(p):]) for p in available_patterns if design.startswith(p))


ans1, ans2 = 0, 0
for design in blocks[1]:
    ans1 += 1 if count_ways(design) else 0
    ans2 += count_ways(design)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

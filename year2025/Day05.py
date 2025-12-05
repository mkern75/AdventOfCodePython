from time import time

time_start = time()
INPUT_FILE = "./year2025/data/day05.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

id_ranges = [tuple(map(int, line.split("-"))) for line in blocks[0]]

ans1 = sum(any(x <= int(line) <= y for x, y in id_ranges) for line in blocks[1])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
id_ranges.sort()
lo, hi = id_ranges[0]
for x, y in id_ranges:
    if x <= hi + 1:
        hi = max(hi, y)
    else:
        ans2 += hi - lo + 1
        lo, hi = x, y
ans2 += hi - lo + 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

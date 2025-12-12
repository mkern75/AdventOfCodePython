from time import time
import re


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


time_start = time()
INPUT_FILE = "./year2025/data/day12.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

shapes = [block[1:] for block in blocks[:-1]]

ans1 = 0
for line in blocks[-1]:
    width, length, *amount = nums(line)
    if (width // 3) * (length // 3) >= sum(amount):
        ans1 += 1
    else:
        s = 0
        for cnt, shape in zip(amount, shapes):
            s += cnt * sum(row.count("#") for row in shape)
        assert s > width * length, "This doesn't work for this input :("
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

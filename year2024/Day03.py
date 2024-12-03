from time import time
import re

time_start = time()
INPUT_FILE = "./year2024/data/day03.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

enabled = True
for line in data:
    for op in re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", line):
        if op.startswith("mul("):
            x, y = map(int, op[4:-1].split(","))
            ans1 += x * y
            if enabled:
                ans2 += x * y
        elif op == "do()":
            enabled = True
        elif op == "don't()":
            enabled = False

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

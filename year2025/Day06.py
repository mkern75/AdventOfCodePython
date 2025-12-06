from time import time
from math import prod

time_start = time()

INPUT_FILE = "./year2025/data/day06.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

n = len(data) - 1
ops, idx = [], []
for i, c in enumerate(data[-1]):
    if c in "+*":
        ops.append(c)
        idx.append(i)
idx.append(max(len(row) for row in data[:-1]) + 1)

ans1, ans2 = 0, 0
for i, op in enumerate(ops):
    width = idx[i + 1] - idx[i]
    nums1 = [int(data[j][idx[i]:idx[i] + width]) for j in range(n)]
    nums2 = []
    for k in range(width - 1):
        s = []
        for j in range(n):
            if idx[i] + k < len(data[j]) and data[j][idx[i] + k] in "0123456789":
                s.append(data[j][idx[i] + k])
        nums2.append(int("".join(s)))
    ans1 += sum(nums1) if op == "+" else prod(nums1)
    ans2 += sum(nums2) if op == "+" else prod(nums2)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

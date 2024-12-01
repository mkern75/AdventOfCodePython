from time import time
from collections import Counter

time_start = time()
INPUT_FILE = "./year2024/data/day01.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

a, b = [], []
for line in data:
    x, y = map(int, line.split())
    a += [x]
    b += [y]
a.sort()
b.sort()
cnt = Counter(b)

ans1 = sum(abs(x - y) for x, y in zip(a, b))
ans2 = sum(x * cnt[x] for x in a)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

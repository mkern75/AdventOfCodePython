from time import time

time_start = time()

INPUT_FILE = "./year2025/data/day03.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


def solve(vals, cnt):
    res, n, idx = 0, len(vals), 0
    for d in range(cnt):
        mx = max(vals[idx:n - (cnt - 1 - d)])
        res = res * 10 + mx
        idx += vals[idx:n - (cnt - 1 - d)].index(mx) + 1
    return res


ans1, ans2 = 0, 0
for row in data:
    vals = list(map(int, list(row)))
    ans1 += solve(vals, 2)
    ans2 += solve(vals, 12)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

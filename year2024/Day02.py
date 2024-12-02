from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day02.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

for line in data:
    a = list(map(int, line.split()))
    n = len(a)

    deltas = {x - y for x, y in zip(a, a[1:])}
    if deltas.issubset({1, 2, 3}) or deltas.issubset({-1, -2, -3}):
        ans1 += 1

    for i in range(n):
        b = a[:i] + a[i + 1:]
        deltas = {x - y for x, y in zip(b, b[1:])}
        if deltas.issubset({1, 2, 3}) or deltas.issubset({-1, -2, -3}):
            ans2 += 1
            break

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

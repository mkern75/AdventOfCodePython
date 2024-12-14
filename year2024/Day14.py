from time import time
import re
from collections import Counter
from math import prod


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


time_start = time()
INPUT_FILE = "./year2024/data/day14.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

X, Y = 101, 103
N = len(data)
x_orig, y_orig, vx, vy = [], [], [], []
for line in data:
    a, b, c, d = nums(line)
    x_orig += [a]
    y_orig += [b]
    vx += [c]
    vy += [d]

x, y = x_orig.copy(), y_orig.copy()
for _ in range(100):
    for i in range(N):
        x[i], y[i] = (x[i] + vx[i]) % X, (y[i] + vy[i]) % Y

cnt = Counter()
for i in range(N):
    if x[i] != X // 2 and y[i] != Y // 2:
        cnt[0 if x[i] < X // 2 else 1, 0 if y[i] < Y // 2 else 1] += 1

ans1 = prod(cnt.values())
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def check_for_tree(pos):
    k = 0
    for (r, c) in pos:
        if (r + 1, c) in pos and (r - 1, c) in pos and (r, c + 1) in pos and (r, c - 1) in pos:
            k += 1
            if k >= 10:
                return True
    return False


def display_tree(x, y):
    g = [["."] * X for _ in range(Y)]
    for xx, yy in zip(x, y):
        g[yy][xx] = "X"
    for row in g:
        print("".join(row))


x, y = x_orig.copy(), y_orig.copy()
seconds = 0
while True:
    seconds += 1
    for i in range(N):
        x[i], y[i] = (x[i] + vx[i]) % X, (y[i] + vy[i]) % Y
    pos = {(x[i], y[i]) for i in range(N)}
    if check_for_tree(pos):
        # display_tree(x, y)
        break

ans2 = seconds
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

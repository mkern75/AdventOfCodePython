from time import time
import re
from collections import Counter
from math import prod

time_start = time()
INPUT_FILE = "./year2024/data/day14.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

width, height = 101, 103
n_robots = len(data)
x_orig, y_orig, vx, vy = [0] * n_robots, [0] * n_robots, [0] * n_robots, [0] * n_robots
for i, line in enumerate(data):
    x_orig[i], y_orig[i], vx[i], vy[i] = map(int, re.findall(r"[-+]?\d+", line))

x, y = x_orig[:], y_orig[:]
for _ in range(100):
    for i in range(n_robots):
        x[i], y[i] = (x[i] + vx[i]) % width, (y[i] + vy[i]) % height

cnt = Counter()
for i in range(n_robots):
    if x[i] != width // 2 and y[i] != height // 2:
        cnt[0 if x[i] < width // 2 else 1, 0 if y[i] < height // 2 else 1] += 1

ans1 = prod(cnt.values())
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def display_tree(x, y):
    g = [["."] * width for _ in range(height)]
    for xx, yy in zip(x, y):
        g[yy][xx] = "X"
    for row in g:
        print("".join(row))


x, y = x_orig[:], y_orig[:]
pos = [[0] * height for _ in range(width)]
seconds = 0
while True:
    seconds += 1
    all_unique_pos = True
    for i in range(n_robots):
        x[i], y[i] = (x[i] + vx[i]) % width, (y[i] + vy[i]) % height
        if pos[x[i]][y[i]] == seconds:
            all_unique_pos = False
        pos[x[i]][y[i]] = seconds
    if all_unique_pos:  # assumption: all robots are at unique positions when the Christmas tree is formed
        # display_tree(x, y)
        break

ans2 = seconds
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

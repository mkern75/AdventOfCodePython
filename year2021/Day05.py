import numpy as np

file = open("./data/year2021/day05.txt", "r")
lines = [line.rstrip('\n') for line in file]


def draw(g, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    n = max(abs(dx), abs(dy))
    for i in range(n + 1):
        g[x1 + i * dx // n][y1 + i * dy // n] += 1


g = np.zeros((1000, 1000), dtype=int)

for line in lines:
    fr, to = line.split(" -> ")
    x1, y1 = map(int, fr.split(","))
    x2, y2 = map(int, to.split(","))
    if x1 == x2 or y1 == y2:
        draw(g, x1, y1, x2, y2)
print(np.count_nonzero(g >= 2))

for line in lines:
    fr, to = line.split(" -> ")
    x1, y1 = map(int, fr.split(","))
    x2, y2 = map(int, to.split(","))
    if x1 != x2 and y1 != y2:
        draw(g, x1, y1, x2, y2)
print(np.count_nonzero(g >= 2))

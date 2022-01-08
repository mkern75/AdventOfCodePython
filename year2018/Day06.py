from utils import load_lines
from math import inf
from collections import Counter

INPUT_FILE = "./year2018/data/day06.txt"


def closest_coord(x, y, coord):
    closest, dist_best = [], inf
    for i, (cx, cy) in coord.items():
        dist = abs(cx - x) + abs(cy - y)
        if dist < dist_best:
            dist_best = dist
            closest = [i]
        elif dist == dist_best:
            closest += [i]
    return closest


def total_dist(x, y, coord):
    dist = 0
    for (cx, cy) in coord.values():
        dist += abs(cx - x) + abs(cy - y)
    return dist


coord = {}
for i, line in enumerate(load_lines(INPUT_FILE)):
    coord[i] = tuple(map(int, line.split(", ")))

x_min = min([x for (x, _) in coord.values()])
x_max = max([x for (x, _) in coord.values()])
y_min = min([y for (_, y) in coord.values()])
y_max = max([y for (_, y) in coord.values()])

area = Counter()
infinite = set()
for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        closest = closest_coord(x, y, coord)
        if len(closest) == 1:
            area[closest[0]] += 1
            if x == x_min or x == x_max or y == y_min or y == y_max:
                infinite.update(closest)

ans1 = 0
for i, c in area.items():
    if i not in infinite:
        ans1 = max(ans1, c)
print("part 1:", ans1)

threshold = 10000
delta = threshold // len(coord) + 1  # we need to check for a slightly larger area, just in case
ans2 = 0
for x in range(x_min - delta, x_max + 1 + delta):
    for y in range(y_min - delta, y_max + 1 + delta):
        if total_dist(x, y, coord) < threshold:
            ans2 += 1
print("part 2:", ans2)

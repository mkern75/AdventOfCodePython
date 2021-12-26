import math

file = open("./year2019/data/day03.txt", "r")
lines = [line.rstrip('\n') for line in file]

DIRECTION = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def visited(wire):
    x, y, c = 0, 0, 0
    v = {}
    for e in wire:
        dx, dy = DIRECTION[e[0]]
        for i in range(int(e[1:])):
            x, y, c = x + dx, y + dy, c + 1
            if (x, y) not in v:
                v[(x, y)] = c
    return v


def manhattan_dist(coord):
    return abs(coord[0]) + abs(coord[1])


wire1 = lines[0].split(",")
wire2 = lines[1].split(",")
visited1 = visited(wire1)
visited2 = visited(wire2)
cross = set(visited1.keys()).intersection(visited2.keys())
ans1, ans2 = math.inf, math.inf
for c in cross:
    ans1 = min(ans1, manhattan_dist(c))
    ans2 = min(ans2, visited1[c] + visited2[c])
print("part 1:", ans1)
print("part 2:", ans2)

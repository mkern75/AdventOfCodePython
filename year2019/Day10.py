from datetime import datetime
import math

# grid representation is as (row,col) here but results require (x,y)

INPUT_FILE = "./year2019/data/day10.txt"


def load_grid(filename):
    file = open(filename, "r")
    lines = [line.rstrip('\n') for line in file]
    return [[c for c in line] for line in lines]


def asteroid(r, c, grid):
    return grid[r][c] == "#"


def visible(r1, c1, r2, c2, grid):
    if (r1, c1) == (r2, c2):
        return False
    if not asteroid(r1, c1, grid) or not asteroid(r2, c2, grid):
        return False
    dr = 0 if r1 == r2 else r2 - r1
    dc = 0 if c1 == c2 else c2 - c1
    gcd = math.gcd(abs(dr), abs(dc))
    for i in range(1, gcd):
        r = r1 + dr // gcd * i
        c = c1 + dc // gcd * i
        if asteroid(r, c, grid):
            return False
    return True


def n_visible(r, c, grid):
    cnt = 0
    for r2 in range(len(grid)):
        for c2 in range(len(grid[0])):
            if visible(r, c, r2, c2, grid):
                cnt += 1
    return cnt


def most_visible(grid):
    n_best, r_best, c_best = 0, 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if asteroid(r, c, grid):
                n = n_visible(r, c, grid)
                if n > n_best:
                    n_best, r_best, c_best = n, r, c
    return n_best, r_best, c_best


def angle(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    a = math.atan2(-(r2 - r1), c2 - c1)  # dy=-delta(row), dx = delta(col)
    if a > math.pi / 2:
        a -= 2 * math.pi
    a -= math.pi / 2
    return abs(a) / math.pi * 180.0


def vaporise(r, c, grid, winner):
    n_vaporised = 0
    while True:
        to_vaporise = []
        for rr in range(len(grid)):
            for cc in range(len(grid[0])):
                if visible(r, c, rr, cc, grid):
                    to_vaporise += [(rr, cc)]
        if len(to_vaporise) == 0:
            break
        to_vaporise = sorted(to_vaporise, key=lambda p: angle((r, c), p))
        while len(to_vaporise) > 0:
            r_vapor, c_vapor = to_vaporise.pop(0)
            n_vaporised += 1
            if n_vaporised == winner:
                return r_vapor, c_vapor
    return None


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

grid = load_grid(INPUT_FILE)

n_best, r_best, c_best = most_visible(grid)
print("part 1:", n_best)

r_vapor, c_vapor = vaporise(r_best, c_best, grid, 200)
print("part 2:", (c_vapor * 100 + r_vapor))

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

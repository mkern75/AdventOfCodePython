from time import time
from grid import Grid

time_start = time()

INPUT_FILE = "./year2024/data/day06.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grid = Grid(data)
r_start, c_start = grid.find("^")

r, c, dir = r_start, c_start, 0
dr, dc = Grid.DIR[dir]
seen_p1 = {(r_start, c_start)}

while True:
    while grid.inside(r + dr, c + dc) and grid.check(r + dr, c + dc, "#"):
        dir = 0 if dir == len(Grid.DIR) - 1 else dir + 1
        dr, dc = Grid.DIR[dir]
    r, c = r + dr, c + dc
    if not grid.inside(r, c):
        break
    seen_p1.add((r, c))

ans1 = len(seen_p1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def state_idx(r, c, dir):
    return dir * grid.R * grid.C + r * grid.C + c


def check_loop_p2(cycle, seen):
    r, c, dir = r_start, c_start, 0
    dr, dc = Grid.DIR[dir]
    while True:
        while grid.inside(r + dr, c + dc) and grid.check(r + dr, c + dc, "#"):
            dir = 0 if dir == len(Grid.DIR) - 1 else dir + 1
            dr, dc = Grid.DIR[dir]
        r, c = r + dr, c + dc
        if not grid.inside(r, c):
            return 0
        if seen[state_idx(r, c, dir)] == cycle:
            return 1
        seen[state_idx(r, c, dir)] = cycle


ans2 = 0
seen = [0] * (4 * grid.R * grid.C)
cycle = 0
for r_obstr, c_obstr in seen_p1:
    if r_obstr == r_start and c_obstr == c_start:
        continue
    cycle += 1
    grid.set(r_obstr, c_obstr, "#")
    ans2 += check_loop_p2(cycle, seen)
    grid.set(r_obstr, c_obstr, ".")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

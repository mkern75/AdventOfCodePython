from utils import load_grid
from collections import defaultdict

INPUT_FILE = "./year2019/data/day24.txt"


def load_initial_state(filename):
    grid = defaultdict(lambda: False)
    g = load_grid(filename)
    for r in range(5):
        for c in range(5):
            grid[r, c] = (g[r][c] == "#")
    return grid


def n_neighbour_bugs_part1(r, c, grid):
    n = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if grid[r + dr, c + dc]:
            n += 1
    return n


def bug(r, c, lvl, grids):
    return 0 if lvl not in grids or not grids[lvl][r, c] else 1


def n_neighbour_bugs_part2(r, c, lvl, grids):
    n = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if r + dr == c + dc == 2:
            if r == 2 and c == 1:
                for rr in range(5):
                    n += bug(rr, 0, lvl + 1, grids)
            if r == 2 and c == 3:
                for rr in range(5):
                    n += bug(rr, 4, lvl + 1, grids)
            if r == 1 and c == 2:
                for cc in range(5):
                    n += bug(0, cc, lvl + 1, grids)
            if r == 3 and c == 2:
                for cc in range(5):
                    n += bug(4, cc, lvl + 1, grids)
        elif 0 <= r + dr < 5 and 0 <= c + dc < 5:
            n += bug(r + dr, c + dc, lvl, grids)
        else:
            if r + dr == -1:
                n += bug(1, 2, lvl - 1, grids)
            if r + dr == 5:
                n += bug(3, 2, lvl - 1, grids)
            if c + dc == -1:
                n += bug(2, 1, lvl - 1, grids)
            if c + dc == 5:
                n += bug(2, 3, lvl - 1, grids)
    return n


def next_state_part1(grid):
    grid_next = defaultdict(lambda: False)
    for r in range(5):
        for c in range(5):
            n = n_neighbour_bugs_part1(r, c, grid)
            if n == 1 or (n == 2 and not grid[r, c]):
                grid_next[r, c] = True
    return grid_next


def biodiversity(grid):
    return sum([2 ** (r * 5 + c) for r in range(5) for c in range(5) if grid[r, c]])


def next_state_part2(grids):
    grids_next = {}
    for lvl, grid in grids.items():
        grids_next[lvl] = defaultdict(lambda: False)
        for r in range(5):
            for c in range(5):
                if not r == c == 2:
                    n = n_neighbour_bugs_part2(r, c, lvl, grids)
                    if n == 1 or (n == 2 and not grid[r, c]):
                        grids_next[lvl][r, c] = True
    level_min, level_max = min(grids_next.keys()), max(grids_next.keys())
    if n_bugs_in_grid(grids_next[level_min]) > 0:
        grids_next[level_min - 1] = defaultdict(lambda: False)
    if n_bugs_in_grid(grids_next[level_max]) > 0:
        grids_next[level_max + 1] = defaultdict(lambda: False)
    return grids_next


def n_bugs_in_grid(grid):
    return sum([1 for r in range(5) for c in range(5) if grid[r, c]])


seen = set()
grid = load_initial_state(INPUT_FILE)
bd = biodiversity(grid)
while bd not in seen:
    seen.add(bd)
    grid = next_state_part1(grid)
    bd = biodiversity(grid)
print("part 1:", bd)

grids = {0: load_initial_state(INPUT_FILE), 1: defaultdict(lambda: False), -1: defaultdict(lambda: False)}
for minute in range(1, 201):
    grids = next_state_part2(grids)
print("part 2:", sum([n_bugs_in_grid(grid) for grid in grids.values()]))

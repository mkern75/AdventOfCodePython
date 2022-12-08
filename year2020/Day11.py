from copy import deepcopy

INPUT_FILE = "./year2020/data/day11.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

DIR = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def occupied1(grid, r, c):
    return sum(0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] == "#" for dr, dc in DIR)


def occupied2(grid, r, c):
    t = 0
    for dr, dc in DIR:
        rr, cc = r, c
        while True:
            rr, cc = rr + dr, cc + dc
            if not (0 <= rr < R and 0 <= cc < C):
                break
            if grid[rr][cc] == "#":
                t += 1
            if grid[rr][cc] != ".":
                break
    return t


def one_cycle(grid, func_occupied, n):
    grid_new = deepcopy(grid)
    for r in range(R):
        for c in range(C):
            occupied = func_occupied(grid, r, c)
            if grid[r][c] == "L" and occupied == 0:
                grid_new[r][c] = "#"
            elif grid[r][c] == "#" and occupied >= n:
                grid_new[r][c] = "L"
    return grid_new, grid_new != grid


grid1, change = deepcopy(grid), True
while change:
    grid1, change = one_cycle(grid1, occupied1, 4)
ans1 = sum(grid1[r][c] == "#" for r in range(R) for c in range(C))
print(f"part 1: {ans1}")

grid2, change = deepcopy(grid), True
while change:
    grid2, change = one_cycle(grid2, occupied2, 5)
ans2 = sum(grid2[r][c] == "#" for r in range(R) for c in range(C))
print(f"part 2: {ans2}")

import numpy as np

file = open("./year2021/data/day09.txt", "r")
lines = [line.rstrip('\n') for line in file]
grid = np.array([[int(c) for c in line] for line in lines])


def basin_size(grid, r, c):
    s = 0
    v = np.zeros((len(grid), len(grid[0])), dtype=bool)
    q = [[r, c]]
    while len(q) > 0:
        rr, cc = q.pop(0)
        if not v[rr][cc] and grid[rr][cc] < 9:
            s += 1
            v[rr][cc] = True
            for rrr, ccc in [(rr - 1, cc), (rr + 1, cc), (rr, cc - 1), (rr, cc + 1)]:
                if 0 <= rrr < len(grid) and 0 <= ccc < len(grid[0]):
                    q.append([rrr, ccc])
    return s


risk, basins = 0, []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        neighbours = []
        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                neighbours.append(grid[rr][cc])
        if grid[r][c] < min(neighbours):
            risk += grid[r][c] + 1
            basins.append(basin_size(grid, r, c))
basins.sort()
print(risk)
print(basins[-1] * basins[-2] * basins[-3])

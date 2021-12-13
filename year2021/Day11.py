import numpy as np

file = open("./year2021/data/day11.txt", "r")
lines = [line.rstrip('\n') for line in file]
grid = np.array([[int(c) for c in line] for line in lines])


def check_flash(grid, r, c):
    if grid[r][c] >= 10:
        grid[r][c] = -1
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < 10 and 0 <= j < 10 and grid[i][j] != -1:
                    grid[i][j] += 1
                    check_flash(grid, i, j)


p1, p2 = -1, -1
step, total = 0, 0
while p1 == -1 or p2 == -1:
    step += 1
    grid = grid + 1
    for r in range(10):
        for c in range(10):
            check_flash(grid, r, c)
    flashes = np.count_nonzero(grid == -1)
    total += flashes
    grid[grid == -1] = 0
    p1 = total if step == 100 else p1
    p2 = step if flashes == 100 else p2
print(p1)
print(p2)

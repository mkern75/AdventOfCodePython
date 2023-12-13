INPUT_FILE = "./year2023/data/day13.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grids = [[]]
for line in data:
    if line:
        grids[-1] += [list(line)]
    else:
        grids += [[]]


def delta_row_symmetrie(grid, row):
    delta = 0
    for r1 in range(row + 1):
        r2 = row + 1 + (row - r1)
        if r2 < len(grid):
            delta += sum(1 for c in range(len(grid[0])) if grid[r1][c] != grid[r2][c])
    return delta


def delta_col_symmetrie(grid, col):
    delta = 0
    for c1 in range(col + 1):
        c2 = col + 1 + (col - c1)
        if c2 < len(grid[0]):
            delta += sum(1 for r in range(len(grid)) if grid[r][c1] != grid[r][c2])
    return delta


ans1, ans2 = 0, 0

for grid in grids:
    for row in range(len(grid) - 1):
        delta = delta_row_symmetrie(grid, row)
        if delta == 0:
            ans1 += 100 * (row + 1)
        elif delta == 1:
            ans2 += 100 * (row + 1)
    for col in range(len(grid[0]) - 1):
        delta = delta_col_symmetrie(grid, col)
        if delta == 0:
            ans1 += col + 1
        elif delta == 1:
            ans2 += col + 1

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

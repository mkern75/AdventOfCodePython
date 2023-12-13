INPUT_FILE = "./year2023/data/day13.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grids = [[]]
for line in data:
    if line:
        grids[-1] += [list(line)]
    else:
        grids += [[]]


def delta_row_symmetry(grid, row):
    delta = 0
    for r1 in range(row + 1):
        r2 = row + 1 + (row - r1)
        if r2 < len(grid):
            delta += sum(1 for c in range(len(grid[0])) if grid[r1][c] != grid[r2][c])
    return delta


def delta_col_symmetry(grid, col):
    return delta_row_symmetry([list(x) for x in zip(*grid)], col)


ans1, ans2 = 0, 0

for grid in grids:
    for row in range(len(grid) - 1):
        delta = delta_row_symmetry(grid, row)
        ans1 += 100 * (row + 1) if delta == 0 else 0
        ans2 += 100 * (row + 1) if delta == 1 else 0
    for col in range(len(grid[0]) - 1):
        delta = delta_col_symmetry(grid, col)
        ans1 += col + 1 if delta == 0 else 0
        ans2 += col + 1 if delta == 1 else 0

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

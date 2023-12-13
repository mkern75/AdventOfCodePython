INPUT_FILE = "./year2023/data/day13.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grids = [[]]
for line in data:
    if line:
        grids[-1] += [list(line)]
    else:
        grids += [[]]


def is_row_reflection(grid, row):
    for r1 in range(row + 1):
        r2 = row + 1 + (row - r1)
        if r2 < len(grid):
            for c in range(len(grid[0])):
                if grid[r1][c] != grid[r2][c]:
                    return False
    return True


def is_col_reflection(grid, col):
    for c1 in range(col + 1):
        c2 = col + 1 + (col - c1)
        if c2 < len(grid[0]):
            for r in range(len(grid)):
                if grid[r][c1] != grid[r][c2]:
                    return False
    return True


ans1, ans2 = 0, 0

for grid in grids:
    R, C = len(grid), len(grid[0])

    reflection_row = next((row for row in range(R - 1) if is_row_reflection(grid, row)), -1)
    if reflection_row != -1:
        ans1 += 100 * (reflection_row + 1)
    reflection_col = next((col for col in range(C - 1) if is_col_reflection(grid, col)), -1)
    if reflection_col != -1:
        ans1 += (reflection_col + 1)

    for r in range(R):
        for c in range(C):
            if grid[r][c] == ".":
                grid[r][c] = "#"
                new_reflection_row = next(
                    (row for row in range(R - 1) if row != reflection_row and is_row_reflection(grid, row)), -1)
                if new_reflection_row != -1:
                    ans2 += 100 * (new_reflection_row + 1)
                new_reflection_col = next(
                    (col for col in range(C - 1) if col != reflection_col and is_col_reflection(grid, col)), -1)
                if new_reflection_col != -1:
                    ans2 += (new_reflection_col + 1)
                grid[r][c] = "."

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

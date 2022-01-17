from utils import load_grid

INPUT_FILE = "./year2020/data/day03.txt"


def n_trees(grid, slope_r, slope_c):
    R, C = len(grid), len(grid[0])
    r, c, n = 0, 0, 0
    while r < R:
        if grid[r][c] == "#":
            n += 1
        r, c = r + slope_r, (c + slope_c) % C
    return n


grid = load_grid(INPUT_FILE)

ans1 = n_trees(grid, 1, 3)
print("part 1:", ans1)

ans2 = n_trees(grid, 1, 1) * n_trees(grid, 1, 3) * n_trees(grid, 1, 5) * n_trees(grid, 1, 7) * n_trees(grid, 2, 1)
print("part 2:", ans2)

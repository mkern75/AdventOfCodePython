from utils import load_grid, tic, toc

INPUT_FILE = "./year2018/data/day18.txt"


def n_neighbours(grid, r, c, what):
    n = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if 0 <= r + dr < R and 0 <= c + dc < C and (r + dr, c + dc) != (r, c):
                if grid[r + dr][c + dc] == what:
                    n += 1
    return n


def update_grid(grid):
    grid_new = [[grid[r][c] for c in range(len(grid))] for r in range(len(grid[0]))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "." and n_neighbours(grid, r, c, "|") >= 3:
                grid_new[r][c] = "|"
            elif grid[r][c] == "|" and n_neighbours(grid, r, c, "#") >= 3:
                grid_new[r][c] = "#"
            elif grid[r][c] == "#" and (n_neighbours(grid, r, c, "#") == 0 or n_neighbours(grid, r, c, "|") == 0):
                grid_new[r][c] = "."
    return grid_new


def grid_to_string(grid):
    return "".join(["".join(row) for row in grid])


tic()
grid = load_grid(INPUT_FILE)
R, C = len(grid), len(grid[0])

for _ in range(10):
    grid = update_grid(grid)

s = grid_to_string(grid)
ans1 = s.count("|") * s.count("#")
print(f"part 1: {ans1}   ({toc():.3f}s)")

# for part two, we iterate until we reach a cycle and then project forward
tic()
grid = load_grid(INPUT_FILE)
m = 0
hist = dict()
hist[grid_to_string(grid)] = m

while True:
    m += 1
    grid = update_grid(grid)
    s = grid_to_string(grid)
    if s in hist:
        cycle_length = m - hist[s]
        break
    else:
        hist[s] = m

idx = m + (1_000_000_000 - m) % cycle_length - cycle_length
ans2 = 0
for key, val in hist.items():
    if val == idx:
        ans2 = key.count("|") * key.count("#")
print(f"part 2: {ans2}   ({toc():.3f}s)")

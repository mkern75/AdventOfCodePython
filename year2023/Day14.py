from copy import deepcopy

INPUT_FILE = "./year2023/data/day14.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


def calc_load(grid):
    R, C = len(grid), len(grid[0])
    return sum(R - r for r in range(R) for c in range(C) if grid[r][c] == "O")


def slide_north(grid):
    R, C = len(grid), len(grid[0])
    for c in range(C):
        for r in range(R):
            if grid[r][c] == "O":
                rr = r
                while rr > 0 and grid[rr - 1][c] == ".":
                    grid[rr - 1][c], grid[rr][c] = "O", "."
                    rr -= 1
    return grid


def rotate_right(grid):
    R, C = len(grid), len(grid[0])
    grid_new = [["."] * R for _ in range(C)]
    for r in range(C):
        for c in range(R):
            grid_new[c][R - 1 - r] = grid[r][c]
    return grid_new


def run_one_cycle(grid):
    for _ in range(4):
        grid = slide_north(grid)
        grid = rotate_right(grid)
    return grid


# part 1
grid = [list(line) for line in data]
grid = slide_north(grid)
ans1 = calc_load(grid)

# part 2
grid = [list(line) for line in data]  # restart
hist = [deepcopy(grid)]
while True:
    grid = run_one_cycle(grid)
    if grid in hist:
        break
    hist += [deepcopy(grid)]

cycles = 1_000_000_000
idx = hist.index(grid)
period = len(hist) - idx
ans2 = calc_load(hist[idx + (cycles - idx) % period])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

from utils import load_lines
from collections import defaultdict

INPUT_FILE = "./year2017/data/day19.txt"


def load_routing(filename):
    routing = defaultdict(lambda: " ")
    lines = load_lines(filename)
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] != " ":
                routing[(r, c)] = lines[r][c]
    return routing


def follow_routing(grid):
    letters, steps = [], 1
    row, col, drow, dcol = 0, min([c for (r, c) in grid.keys() if r == 0]), 1, 0

    while True:
        if grid[row, col].isalpha():  # record letter
            letters += [grid[row, col]]

        row_next, col_next, drow_next, dcol_next = row + drow, col + dcol, drow, dcol
        if grid[row_next, col_next] != " ":  # straight on
            row, col, drow, dcol = row_next, col_next, drow_next, dcol_next
            steps += 1
            continue

        row_next, col_next, drow_next, dcol_next = row + dcol, col - drow, dcol, -drow
        if grid[row_next, col_next] != " ":  # turn right
            row, col, drow, dcol = row_next, col_next, drow_next, dcol_next
            steps += 1
            continue

        row_next, col_next, drow_next, dcol_next = row - dcol, col + drow, -dcol, drow
        if grid[row_next, col_next] != " ":  # turn left
            row, col, drow, dcol = row_next, col_next, drow_next, dcol_next
            steps += 1
            continue

        break

    return "".join(letters), steps


routing = load_routing(INPUT_FILE)

ans1, ans2 = follow_routing(routing)
print("part 1:", ans1)
print("part 2:", ans2)

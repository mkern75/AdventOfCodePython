from time import time

time_start = time()

SHOW_GRID = False

INPUT_FILE = "./year2024/data/day15.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


def display_grid(info):
    if SHOW_GRID:
        print(info)
        for r in range(R):
            row = []
            for c in range(C):
                row += ["@" if r == r_robot and c == c_robot else grid[r][c]]
            print("".join(row))
        print()


def scale_up_grid():
    global grid, R, C, r_robot, c_robot
    g = [["."] * (2 * C) for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] in "#.":
                g[r][2 * c] = grid[r][c]
                g[r][2 * c + 1] = grid[r][c]
            elif grid[r][c] == "O":
                g[r][2 * c] = "["
                g[r][2 * c + 1] = "]"
            elif grid[r][c] == "@":
                g[r][2 * c] = "@"
                g[r][2 * c + 1] = "."
    grid = g
    C *= 2
    c_robot *= 2


def move_horizontally(dc):
    global grid, r_robot, c_robot

    if grid[r_robot][c_robot + dc] == "#":
        return

    if grid[r_robot][c_robot + dc] == ".":
        c_robot += dc
        return

    cc = c_robot + dc
    while grid[r_robot][cc] in "O[]":
        cc += dc

    if grid[r_robot][cc] != ".":
        return

    for c in range(cc, c_robot, -dc):
        grid[r_robot][c] = grid[r_robot][c - dc]
    grid[r_robot][c_robot + dc] = "."
    c_robot += dc


def move_vertically(dr):
    global grid, r_robot, c_robot

    if grid[r_robot + dr][c_robot] == "#":
        return

    if grid[r_robot + dr][c_robot] == ".":
        r_robot += dr
        return

    rr = r_robot + dr
    while grid[rr][c_robot] in "O[]":
        rr += dr

    if grid[rr][c_robot] != ".":
        return

    for r in range(rr, r_robot, -dr):
        grid[r][c_robot] = grid[r - dr][c_robot]
    grid[r_robot + dr][c_robot] = "."
    r_robot += dr


def move_vertically_part2(dr):
    global grid, r_robot, c_robot

    if grid[r_robot + dr][c_robot] == "#":
        return

    if grid[r_robot + dr][c_robot] == ".":
        r_robot += dr
        return

    boxes = set()
    if grid[r_robot + dr][c_robot] == "[":
        boxes.add((r_robot + dr, c_robot))
        boxes.add((r_robot + dr, c_robot + 1))
    if grid[r_robot + dr][c_robot] == "]":
        boxes.add((r_robot + dr, c_robot - 1))
        boxes.add((r_robot + dr, c_robot))

    while True:
        additional_boxes = set()
        for r, c in boxes:
            if grid[r + dr][c] in "[]" and (r + dr, c) not in boxes:
                if grid[r + dr][c] == "[":
                    additional_boxes.add((r + dr, c))
                    additional_boxes.add((r + dr, c + 1))
                if grid[r + dr][c] == "]":
                    additional_boxes.add((r + dr, c - 1))
                    additional_boxes.add((r + dr, c))
        boxes.update(additional_boxes)
        if not additional_boxes:
            break

    move_possible = True
    for r, c in boxes:
        if (r + dr, c) not in boxes and grid[r + dr][c] != ".":
            move_possible = False

    if not move_possible:
        return

    boxes = sorted(boxes, reverse=(dr == 1))
    for r, c in boxes:
        grid[r + dr][c] = grid[r][c]
        grid[r][c] = "."
        display_grid(f"{r}/{c}")
    r_robot += dr


def gps():
    return sum(100 * r + c for r in range(R) for c in range(C) if grid[r][c] in "O[")


# *********************************************************
# PART 1
grid = [list(line.rstrip("\n")) for line in blocks[0]]
R, C = len(grid), len(grid[0])
moves = list("".join(blocks[1]))

r_robot, c_robot = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "@")
grid[r_robot][c_robot] = "."

display_grid("start")
for i, m in enumerate(moves, start=1):
    if m == "^":
        move_vertically(-1)
    elif m == "v":
        move_vertically(+1)
    elif m == "<":
        move_horizontally(-1)
    elif m == ">":
        move_horizontally(+1)
    display_grid(f"move {i}: {m}")

ans1 = gps()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# *********************************************************
# PART 2
grid = [list(line.rstrip("\n")) for line in blocks[0]]
R, C = len(grid), len(grid[0])
moves = list("".join(blocks[1]))

r_robot, c_robot = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "@")
grid[r_robot][c_robot] = "."

scale_up_grid()

display_grid("start")
for i, m in enumerate(moves, start=1):
    if m == "^":
        move_vertically_part2(-1)
    elif m == "v":
        move_vertically_part2(+1)
    elif m == "<":
        move_horizontally(-1)
    elif m == ">":
        move_horizontally(+1)
    display_grid(f"move {i}: {m}")

ans2 = gps()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

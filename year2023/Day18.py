from collections import defaultdict

INPUT_FILE = "./year2023/data/day18.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

MOVE = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0),
        "2": (0, -1), "0": (0, 1), "3": (-1, 0), "1": (1, 0)}


def solve(instructions):
    # trench polygon: list of line segments (row1, col1, row2, col2)
    row, col, polygon = 0, 0, []
    row_coord, col_coord = {0, 1}, {0, 1}
    for direction, distance in instructions:
        polygon += [(row, col, row + distance * MOVE[direction][0], col + distance * MOVE[direction][1])]
        row, col = polygon[-1][2], polygon[-1][3]
        row_coord |= {row, row + 1}
        col_coord |= {col, col + 1}

    # coordinate compression
    row_coord = sorted(row_coord)
    row_idx = {v: i for i, v in enumerate(row_coord)}
    col_coord = sorted(col_coord)
    col_idx = {v: i for i, v in enumerate(col_coord)}

    # build plan with compressed coordinates
    plan = defaultdict(lambda: ".")
    for r1, c1, r2, c2 in polygon:
        r1, c1, r2, c2 = row_idx[r1], col_idx[c1], row_idx[r2], col_idx[c2]
        for r in range(min(r1, r2), max(r1, r2) + 1):
            for c in range(min(c1, c2), max(c1, c2) + 1):
                plan[r, c] = "#"

    # floodfill outside of polygon with "X"
    r_min, r_max = min(r for r, _ in plan) - 1, max(r for r, _ in plan) + 1
    c_min, c_max = min(c for _, c in plan) - 1, max(c for _, c in plan) + 1
    q = [(r_min, c_min)]  # definitely outside
    while q:
        r, c = q.pop()
        if r_min <= r <= r_max and c_min <= c <= c_max and plan[r, c] == ".":
            plan[r, c] = "X"
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q += [(r + dr, c + dc)]

    # calculate result by reverting back to original coordinates
    res = 0
    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            if plan[r, c] != "X":  # not outside => inside
                res += (row_coord[r + 1] - row_coord[r]) * (col_coord[c + 1] - col_coord[c])
    return res


# part 1
instructions = [(line.split()[0], int(line.split()[1])) for line in data]
ans1 = solve(instructions)
print(f"part 1: {ans1}")

# part 2
instructions = [(line.split()[2][7], int(line.split()[2][2:7], 16)) for line in data]
ans2 = solve(instructions)
print(f"part 2: {ans2}")

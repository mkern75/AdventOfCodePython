from collections import defaultdict

INPUT_FILE = "./year2023/data/day18.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

DIR = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0),
       "2": (0, -1), "0": (0, 1), "3": (-1, 0), "1": (1, 0)}


def solve(instructions):
    # construct polygon
    polygon = []
    row, col = 0, 0
    coordinate_set = {0, 1}
    for direction, distance in instructions:
        row_next = row + distance * DIR[direction][0]
        col_next = col + distance * DIR[direction][1]
        polygon += [(row, col, row_next, col_next)]
        row = row_next
        col = col_next
        coordinate_set |= {row, row + 1, col, col + 1}

    # coordinate compression
    coordinates = sorted(coordinate_set)
    idx_coord = {v: i for i, v in enumerate(coordinates)}

    # build plan with compressed coordinates
    plan = defaultdict(lambda: ".")
    for r1, c1, r2, c2 in polygon:
        rr1, cc1, rr2, cc2 = idx_coord[r1], idx_coord[c1], idx_coord[r2], idx_coord[c2]
        for r in range(min(rr1, rr2), max(rr1, rr2) + 1):
            for c in range(min(cc1, cc2), max(cc1, cc2) + 1):
                plan[r, c] = "#"

    # floodfill outside of polygon with "X"
    r_min, r_max = min(r for (r, _) in plan) - 1, max(r for (r, _) in plan) + 1
    c_min, c_max = min(c for (_, c) in plan) - 1, max(c for (_, c) in plan) + 1
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
                res += (coordinates[r + 1] - coordinates[r]) * (coordinates[c + 1] - coordinates[c])
    return res


# part 1
instructions = [(line.split()[0], int(line.split()[1])) for line in data]
ans1 = solve(instructions)
print(f"part 1: {ans1}")

# part 2
instructions = [(line.split()[2][7], int(line.split()[2][2:7], 16)) for line in data]
ans2 = solve(instructions)
print(f"part 2: {ans2}")

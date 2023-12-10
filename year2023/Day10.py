from collections import defaultdict

INPUT_FILE = "./year2023/data/day10.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

CONNECTS = {"-": [(0, -1), (0, +1)], "|": [(-1, 0), (+1, 0)], "F": [(+1, 0), (0, +1)], "7": [(+1, 0), (0, -1)],
            "L": [(-1, 0), (0, +1)], "J": [(-1, 0), (0, -1)]}
PIPES = CONNECTS.keys()

# grid
grid = defaultdict(lambda: ".")
R, C = len(data), len(data[0])
for r, line in enumerate(data):
    for c, x in enumerate(line):
        grid[r, c] = x

# start row and column
r_start, c_start = next((r, c) for r in range(R) for c in range(C) if grid[r, c] == "S")

# find loop
for start_pipe in PIPES:
    loop = [(r_start, c_start), (r_start + CONNECTS[start_pipe][0][0], c_start + CONNECTS[start_pipe][0][1])]
    loop_found = False
    while True:
        if loop[-1] == loop[0]:
            loop_found = True
            break
        if grid[loop[-1]] not in PIPES:
            break
        (r, c), pipe = loop[-1], grid[loop[-1]]
        if loop[-2] == (r + CONNECTS[pipe][0][0], c + CONNECTS[pipe][0][1]):
            loop += [(r + CONNECTS[pipe][1][0], c + CONNECTS[pipe][1][1])]
        elif loop[-2] == (r + CONNECTS[pipe][1][0], c + CONNECTS[pipe][1][1]):
            loop += [(r + CONNECTS[pipe][0][0], c + CONNECTS[pipe][0][1])]
        else:
            break
    if loop_found:
        grid[r_start, c_start] = start_pipe
        loop = set(loop)
        break
else:
    assert False

ans1 = len(loop) // 2

ans2 = 0
for r in range(R):
    # count how often the loop crosses the current row
    # the row is crossed when encountering loop segments "|", "L-7" or "F-J" (any number of "-")
    # if the current row has been crossed an odd number of times when reaching a column, that tile is inside the loop
    is_inside, prev_pipe = 0, "."
    for c in range(C):
        if (r, c) in loop:
            if grid[r, c] == "|":
                is_inside = 1 - is_inside
            elif grid[r, c] in ["L", "F"]:
                prev_pipe = grid[r, c]
            elif prev_pipe == "L" and grid[r, c] == "7":
                is_inside = 1 - is_inside
            elif prev_pipe == "F" and grid[r, c] == "J":
                is_inside = 1 - is_inside
        else:
            ans2 += is_inside

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

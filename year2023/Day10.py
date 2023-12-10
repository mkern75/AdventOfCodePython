INPUT_FILE = "./year2023/data/day10.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

PIPE_CONNECTIONS = {"-": [(0, -1), (0, +1)], "|": [(-1, 0), (+1, 0)], "F": [(+1, 0), (0, +1)],
                    "7": [(+1, 0), (0, -1)], "L": [(-1, 0), (0, +1)], "J": [(-1, 0), (0, -1)]}

# grid and start row/column
grid = [list(line) for line in data]
R, C = len(grid), len(grid[0])
r_start, c_start = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")

# find loop
for start_pipe, start_connect in PIPE_CONNECTIONS.items():
    path = [(r_start, c_start), (r_start + start_connect[0][0], c_start + start_connect[0][1])]
    loop_found = False
    while True:
        r, c = path[-1]
        if not (0 <= r < R and 0 <= c < C) or grid[r][c] == ".":
            break
        if (r, c) == (r_start, c_start):
            loop_found = True
            break
        connect = PIPE_CONNECTIONS[grid[r][c]]
        if path[-2] == (r + connect[0][0], c + connect[0][1]):
            path += [(r + connect[1][0], c + connect[1][1])]
        elif path[-2] == (r + connect[1][0], c + connect[1][1]):
            path += [(r + connect[0][0], c + connect[0][1])]
        else:
            break
    if loop_found:
        grid[r_start][c_start] = start_pipe
        loop = set(path)
        ans1 = len(loop) // 2
        break
else:
    assert False

# adapted version of ray-casting algorithm for point-in-polygon problem
ans2 = 0
for r in range(R):
    is_inside, prev = 0, "."
    for c in range(C):
        if (r, c) in path:
            if grid[r][c] in ["L", "F"]:
                prev = grid[r][c]
            elif grid[r][c] == "|" or (prev == "L" and grid[r][c] == "7") or (prev == "F" and grid[r][c] == "J"):
                is_inside = 1 - is_inside
        else:
            ans2 += is_inside

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

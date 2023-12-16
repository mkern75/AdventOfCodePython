INPUT_FILE = "./year2023/data/day16.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
R, C = len(grid), len(grid[0])


def simulate(r_init, c_init, dr_init, dc_init):
    seen = set()
    q = [(r_init, c_init, dr_init, dc_init)]
    while q:
        r, c, dr, dc = q.pop()
        if 0 <= r < R and 0 <= c < C and (r, c, dr, dc) not in seen:
            seen |= {(r, c, dr, dc)}
            if grid[r][c] == "\\":
                q += [(r + dc, c + dr, dc, dr)]
            elif grid[r][c] == "/":
                q += [(r - dc, c - dr, -dc, -dr)]
            elif grid[r][c] == "-" and dr != 0:
                q += [(r, c - 1, 0, -1), (r, c + 1, 0, 1)]
            elif grid[r][c] == "|" and dc != 0:
                q += [(r + 1, c, 1, 0), (r - 1, c, -1, 0)]
            else:
                q += [(r + dr, c + dc, dr, dc)]  # default
    return len({(r, c) for r, c, _, _ in seen})


ans1 = simulate(0, 0, 0, 1)
print(f"part 1: {ans1}")

ans2 = max(max(simulate(0, c, 1, 0) for c in range(C)),
           max(simulate(R - 1, c, -1, 0) for c in range(C)),
           max(simulate(r, 0, 0, 1) for r in range(R)),
           max(simulate(r, C - 1, 0, -1) for r in range(R)))
print(f"part 2: {ans2}")

INPUT_FILE = "./year2023/data/day16.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
R, C = len(grid), len(grid[0])


def simulate(r, c, dr, dc):
    energised = [[0] * C for _ in range(R)]
    seen = set()
    q = [(r, c, dr, dc)]
    while q:
        r, c, dr, dc = q.pop()
        assert abs(dr) + abs(dc) == 1
        if not (0 <= r < R and 0 <= c < C) or (r, c, dr, dc) in seen:
            continue
        seen |= {(r, c, dr, dc)}
        energised[r][c] = 1

        if grid[r][c] == ".":
            q += [(r + dr, c + dc, dr, dc)]
        elif grid[r][c] == "\\":
            if dc == 1:
                q += [(r + 1, c, 1, 0)]
            elif dc == -1:
                q += [(r - 1, c, -1, 0)]
            elif dr == 1:
                q += [(r, c + 1, 0, 1)]
            elif dr == -1:
                q += [(r, c - 1, 0, -1)]
        elif grid[r][c] == "/":
            if dc == 1:
                q += [(r - 1, c, -1, 0)]
            elif dc == -1:
                q += [(r + 1, c, 1, 0)]
            elif dr == 1:
                q += [(r, c - 1, 0, -1)]
            elif dr == -1:
                q += [(r, c + 1, 0, 1)]
        elif grid[r][c] == "-":
            if dc != 0:
                q += [(r + dr, c + dc, dr, dc)]
            elif dr != 0:
                q += [(r, c - 1, 0, -1), (r, c + 1, 0, 1)]
        elif grid[r][c] == "|":
            if dr != 0:
                q += [(r + dr, c + dc, dr, dc)]
            elif dc != 0:
                q += [(r + 1, c, 1, 0), (r - 1, c, -1, 0)]
    return sum(sum(row) for row in energised)


ans1 = simulate(0, 0, 0, 1)
print(f"part 1: {ans1}")

ans2 = max(max(simulate(0, c, 1, 0) for c in range(C)),
           max(simulate(R - 1, c, -1, 0) for c in range(C)),
           max(simulate(r, 0, 0, 1) for r in range(R)),
           max(simulate(r, C - 1, 0, -1) for r in range(R)))
print(f"part 2: {ans2}")

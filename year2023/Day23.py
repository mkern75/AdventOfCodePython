from collections import defaultdict

INPUT_FILE = "./year2023/data/day23.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

MOVES = {".": [(1, 0), (-1, 0), (0, 1), (0, -1)], ">": [(0, 1)], "<": [(0, -1)], "^": [(-1, 0)], "v": [(1, 0)], "#": []}

r_start, c_start = 0, next(c for c in range(C) if grid[0][c] == ".")
r_end, c_end = R - 1, next(c for c in range(C) if grid[R - 1][c] == ".")


def find_longest_path(r_start, c_start, r_end, c_end, adj):
    res = 0
    q = [(r_start, c_start, 0, {(r_start, c_start)})]
    while q:
        r, c, dist, visited = q.pop()
        if (r, c) == (r_end, c_end):
            res = max(res, dist)
        else:
            for rn, cn, dn in adj[r, c]:
                if (rn, cn) not in visited:
                    q += [(rn, cn, dist + dn, visited | {(rn, cn)})]
    return res


# part 1: brute force
adj1 = defaultdict(list)
for r in range(R):
    for c in range(C):
        for dr, dc in MOVES[grid[r][c]]:
            rn, cn = r + dr, c + dc
            if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                adj1[r, c] += [(rn, cn, 1)]

ans1 = find_longest_path(r_start, c_start, r_end, c_end, adj1)
print(f"part 1: {ans1}")

# part 2: only consider grid positions / junctions with an actual choice or cul-de-sacs
pos = []
for r in range(R):
    for c in range(C):
        if grid[r][c] != "#":
            if sum(1 for dr, dc in MOVES["."] if
                   0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] != "#") != 2:
                pos += [(r, c)]

adj2 = defaultdict(list)
for rv, cv in pos:
    visited = set()
    q = [(rv, cv, 0)]
    while q:
        r, c, dist = q.pop()
        if (r, c) not in visited:
            visited |= {(r, c)}
            if (r, c) != (rv, cv) and (r, c) in pos:
                adj2[rv, cv] += [(r, c, dist)]
            else:
                for dr, dc in MOVES["."]:
                    rn, cn = r + dr, c + dc
                    if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                        q += [(rn, cn, dist + 1)]

ans2 = find_longest_path(r_start, c_start, r_end, c_end, adj2)
print(f"part 2: {ans2}")

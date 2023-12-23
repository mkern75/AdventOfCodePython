# v2 for speed: runs in ~1s using pypy on MacBook Pro 2021

from collections import defaultdict

INPUT_FILE = "./year2023/data/day23.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

MOVES1 = {".": [(1, 0), (-1, 0), (0, 1), (0, -1)], ">": [(0, 1)], "<": [(0, -1)], "^": [(-1, 0)], "v": [(1, 0)]}
MOVES2 = {c: MOVES1["."] for c in ".<>^v"}

# start and end grid coordinates
start = (0, next(c for c in range(C) if grid[0][c] == "."))
end = (R - 1, next(c for c in range(C) if grid[R - 1][c] == "."))

#  points-of-interest: only consider grid coordinates with an actual choice, i.e. junctions, plus start and end
poi = [start, end]
for r in range(R):
    for c in range(C):
        if grid[r][c] != "#":
            if sum(1 for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] if
                   0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#") > 2:
                poi += [(r, c)]
N = len(poi)
idx = {p: i for i, p in enumerate(poi)}
start_idx = idx[start]
end_idx = idx[end]


def build_adjacency_list(moves):
    adj = defaultdict(list)
    for i in range(N):
        visited = set()
        q = [(poi[i][0], poi[i][1], 0)]
        while q:
            r, c, dist = q.pop()
            if (r, c) not in visited:
                visited |= {(r, c)}
                if (r, c) != poi[i] and (r, c) in idx:
                    adj[i] += [(idx[r, c], dist)]
                else:
                    for dr, dc in moves[grid[r][c]]:
                        rn, cn = r + dr, c + dc
                        if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                            q += [(rn, cn, dist + 1)]
    return adj


def find_longest_path(adj):
    res = 0
    q = [(start_idx, 0, 1 << start_idx)]
    while q:
        v, dist_so_far, visited = q.pop()
        if v == end_idx:
            res = max(res, dist_so_far)
        else:
            for vn, dist_to_vn in adj[v]:
                if visited & (1 << vn) == 0:
                    q += [(vn, dist_so_far + dist_to_vn, visited | (1 << vn))]
    return res


# part 1
adj1 = build_adjacency_list(MOVES1)
ans1 = find_longest_path(adj1)
print(f"part 1: {ans1}")

# part 2
adj2 = build_adjacency_list(MOVES2)
ans2 = find_longest_path(adj2)
print(f"part 2: {ans2}")

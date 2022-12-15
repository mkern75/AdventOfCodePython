INPUT_FILE = "./year2022/data/day12.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])
rs, cs = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")
re, ce = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "E")
grid[rs][cs], grid[re][ce] = "a", "z"


def bfs1(start, end):
    return bfs2([start], end)


def bfs2(starts, end):
    q, v = [], set()
    for (rs, cs) in starts:
        q += [(0, rs, cs)]
        v |= {(rs, cs)}
    while q:
        n, r, c = q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C:
                if (r + dr, c + dc) not in v and ord(grid[r][c]) + 1 >= ord(grid[r + dr][c + dc]):
                    if (r + dr, c + dc) == end:
                        return n + 1
                    q += [(n + 1, r + dr, c + dc)]
                    v |= {(r + dr, c + dc)}
    return -1


ans1 = bfs1((rs, cs), (re, ce))
print(f"part 1: {ans1}")

starts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == "a"]
ans2 = bfs2(starts, (re, ce))
print(f"part 2: {ans2}")
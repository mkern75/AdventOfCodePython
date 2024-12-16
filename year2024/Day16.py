from time import time
from collections import defaultdict
from heapq import heappop, heappush

time_start = time()

INPUT_FILE = "./year2024/data/day16.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

INF = 1 << 31

r_start, c_start, r_end, c_end = 0, 0, 0, 0
dr_start, dc_start = 0, 1
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            r_start, c_start = r, c
        if grid[r][c] == "E":
            r_end, c_end = r, c

dist = defaultdict(lambda: INF)
prev = defaultdict(set)

dist[r_start, c_start, dr_start, dc_start] = 0
q = [(0, r_start, c_start, dr_start, dc_start)]

ans1 = INF

while q:
    d, r, c, dr, dc = heappop(q)

    if d > dist[r, c, dr, dc]:
        continue

    if d > ans1:
        break

    if r == r_end and c == c_end:
        ans1 = d

    r_next, c_next = r + dr, c + dc
    if grid[r + dr][c + dc] != "#":
        d_next = dist[r_next, c_next, dr, dc]
        if d + 1 < d_next:
            heappush(q, (d + 1, r_next, c_next, dr, dc))
            dist[r_next, c_next, dr, dc] = d + 1
            prev[r_next, c_next, dr, dc].add((r, c, dr, dc))
        elif d + 1 == d_next:
            prev[r_next, c_next, dr, dc].add((r, c, dr, dc))

    for dr_next, dc_next in [(dc, -dr), (-dc, dr)]:
        d_next = dist[r, c, dr_next, dc_next]
        if d + 1000 < d_next:
            heappush(q, (d + 1000, r, c, dr_next, dc_next))
            dist[r, c, dr_next, dc_next] = d + 1000
            prev[r, c, dr_next, dc_next].add((r, c, dr, dc))
        elif d + 1000 == d_next:
            prev[r, c, dr_next, dc_next].add((r, c, dr, dc))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

seen = {(r_end, c_end, 1, 0), (r_end, c_end, 0, 1), (r_end, c_end, -1, 0), (r_end, c_end, 0, -1)}
seen2 = {(r_end, c_end)}
q = [(r_end, c_end, 1, 0), (r_end, c_end, 0, 1), (r_end, c_end, -1, 0), (r_end, c_end, 0, -1)]

while q:
    r, c, dr, dc = q.pop()
    for (rr, cc, drr, dcc) in prev[r, c, dr, dc]:
        if (rr, cc, drr, dcc) not in seen:
            seen.add((rr, cc, drr, dcc))
            seen2.add((rr, cc))
            q.append((rr, cc, drr, dcc))

ans2 = len(seen2)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

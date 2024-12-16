from time import time
from collections import defaultdict
from heapq import heappop, heappush

time_start = time()

INPUT_FILE = "./year2024/data/day16.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

INF = 1 << 31
ans1 = INF

r_start, c_start, r_end, c_end = 0, 0, 0, 0
dr_start, dc_start = 0, 1
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            r_start, c_start = r, c
        if grid[r][c] == "E":
            r_end, c_end = r, c

dist = defaultdict(lambda: INF)
dist[r_start, c_start, dr_start, dc_start] = 0
prev = defaultdict(set)

q = [(0, r_start, c_start, dr_start, dc_start)]
while q:
    d, r, c, dr, dc = heappop(q)

    if d > dist[r, c, dr, dc]:
        continue

    if d > ans1:
        break

    if r == r_end and c == c_end:
        ans1 = d

    for r_next, c_next, dr_next, dc_next, cost in [(r + dr, c + dc, dr, dc, 1),
                                                   (r, c, dc, -dr, 1000),
                                                   (r, c, -dc, dr, 1000)]:
        if grid[r_next][c_next] != "#":
            dist_next = dist[r_next, c_next, dr_next, dc_next]
            if d + cost < dist_next:
                heappush(q, (d + cost, r_next, c_next, dr_next, dc_next))
                dist[r_next, c_next, dr_next, dc_next] = d + cost
                prev[r_next, c_next, dr_next, dc_next].add((r, c, dr, dc))
            elif d + cost == dist_next:
                prev[r_next, c_next, dr_next, dc_next].add((r, c, dr, dc))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

seen = {(r_end, c_end, 1, 0), (r_end, c_end, 0, 1), (r_end, c_end, -1, 0), (r_end, c_end, 0, -1)}
q = [(r_end, c_end, 1, 0), (r_end, c_end, 0, 1), (r_end, c_end, -1, 0), (r_end, c_end, 0, -1)]
while q:
    r, c, dr, dc = q.pop()
    for (r_prev, c_prev, dr_prev, dc_prev) in prev[r, c, dr, dc]:
        if (r_prev, c_prev, dr_prev, dc_prev) not in seen:
            seen.add((r_prev, c_prev, dr_prev, dc_prev))
            q.append((r_prev, c_prev, dr_prev, dc_prev))

ans2 = len({(r, c) for r, c, _, _ in seen})
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

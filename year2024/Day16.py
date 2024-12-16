from time import time
from heapq import heappop, heappush

time_start = time()

INPUT_FILE = "./year2024/data/day16.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])


def ff(dist, row, col, dir):
    return (dist << 32) | (row << 20) | (col << 8) | dir


def fr(x):
    return x >> 32, (x >> 20) & 0xFFF, (x >> 8) & 0xFFF, x & 0xFF


def idx(row, col, dir):
    return dir * R * C + row * C + col


INF = 1 << 63
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

r_start, c_start, dir_start = 0, 0, 0
r_end, c_end = 0, 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            r_start, c_start = r, c
        if grid[r][c] == "E":
            r_end, c_end = r, c

dist = [INF] * (4 * R * C)
prev = [set() for _ in range(4 * R * C)]

dist[idx(r_start, c_start, dir_start)] = 0
q = [ff(0, r_start, c_start, dir_start)]
ans1 = INF

while q:
    d, r, c, dir = fr(heappop(q))

    if d > dist[idx(r, c, dir)]:
        continue

    if d > ans1:
        break

    if r == r_end and c == c_end:
        ans1 = d

    dr, dc = DIR[dir]
    for r_next, c_next, dir_next, cost in [(r + dr, c + dc, dir, 1),
                                           (r, c, (dir + 1) % 4, 1000),
                                           (r, c, (dir - 1) % 4, 1000)]:
        if grid[r_next][c_next] == "#":
            continue
        dist_next = dist[idx(r_next, c_next, dir_next)]
        if d + cost < dist_next:
            heappush(q, ff(d + cost, r_next, c_next, dir_next))
            dist[idx(r_next, c_next, dir_next)] = d + cost
            prev[idx(r_next, c_next, dir_next)] = {(r, c, dir)}
        elif d + cost == dist_next:
            prev[idx(r_next, c_next, dir_next)].add((r, c, dir))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

seen = {(r_end, c_end, dir) for dir in range(4) if dist[idx(r_end, c_end, dir)] == ans1}
q = [(r_end, c_end, dir) for dir in range(4) if dist[idx(r_end, c_end, dir)] == ans1]
while q:
    r, c, dir = q.pop()
    for (r_prev, c_prev, dir_prev) in prev[idx(r, c, dir)]:
        if (r_prev, c_prev, dir_prev) not in seen:
            seen.add((r_prev, c_prev, dir_prev))
            q.append((r_prev, c_prev, dir_prev))

ans2 = len({(r, c) for r, c, _ in seen})
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

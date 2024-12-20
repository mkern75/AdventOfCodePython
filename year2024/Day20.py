from time import time

time_start = time()

INF = 1 << 31

INPUT_FILE = "./year2024/data/day20.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])


def find(target):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == target:
                return r, c
    return -1, -1


def calc_dist(r_start, c_start):
    dist = [[INF] * C for _ in range(R)]
    dist[r_start][c_start] = 0
    bfs = [(r_start, c_start)]
    for r, c in bfs:
        for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= r and r < R and 0 <= c and c < C:
                if grid[rn][cn] != "#" and dist[rn][cn] == INF:
                    dist[rn][cn] = dist[r][c] + 1
                    bfs.append((rn, cn))
    return dist


r_start, c_start = find("S")
dist_start = calc_dist(r_start, c_start)

r_end, c_end = find("E")
dist_end = calc_dist(r_end, c_end)

normal_time = dist_start[r_end][c_end]


def solve(max_cheat, min_saving):
    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "#":
                continue
            for rn in range(max(0, r - max_cheat), min(R, r + max_cheat + 1)):
                dr = abs(r - rn)
                cheat_remaining = max_cheat - dr
                for cn in range(max(0, c - cheat_remaining), min(C, c + cheat_remaining + 1)):
                    if grid[rn][cn] == "#":
                        continue
                    dc = abs(c - cn)
                    cheat_step = dr + dc
                    cheat_time = dist_start[r][c] + cheat_step + dist_end[rn][cn]
                    if cheat_time <= normal_time - min_saving:
                        res += 1
    return res


ans1 = solve(2, 100)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = solve(20, 100)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

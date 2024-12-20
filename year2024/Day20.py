from time import time

time_start = time()

INF = 1 << 31

INPUT_FILE = "./year2024/data/day20.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])


def valid_row(r):
    return 0 <= r and r < R


def valid_col(c):
    return 0 <= c and c < C


def valid(r, c):
    return valid_row(r) and valid_col(c)


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
            if valid(rn, cn) and grid[rn][cn] != "#" and dist[rn][cn] == INF:
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
        for dr in range(-max_cheat, max_cheat + 1):
            rn = r + dr
            if not valid_row(rn):
                continue
            cheat_remaining = max_cheat - abs(dr)
            for c in range(C):
                for dc in range(-cheat_remaining, cheat_remaining + 1):
                    cn = c + dc
                    if not valid_col(cn):
                        continue
                    if grid[rn][cn] == "#":
                        continue
                    cheat_dist = abs(dr) + abs(dc)
                    cheat_time = dist_start[r][c] + cheat_dist + dist_end[rn][cn]
                    if cheat_time <= normal_time - min_saving:
                        res += 1
    return res


ans1 = solve(2, 100)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = solve(20, 100)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

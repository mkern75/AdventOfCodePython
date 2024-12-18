from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day18.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

byte_pos = [tuple(map(int, line.split(","))) for line in data]

R, C = 71, 71
BYTES_PART_1 = 1024
r_start, c_start = 0, 0
r_end, c_end = R - 1, C - 1

safe = [[1 << 31] * C for _ in range(R)]
for t, (c, r) in enumerate(byte_pos, start=1):
    safe[r][c] = t


def run_bfs(max_unsafe):
    bfs = [(r_start, c_start, 0)]
    seen = [[False] * C for _ in range(R)]
    seen[r_start][c_start] = True
    for r, c, t in bfs:
        if r == r_end and c == c_end:
            return t
        for rn, cn in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < R and 0 <= cn < C:
                if safe[rn][cn] > max_unsafe and not seen[rn][cn]:
                    bfs += [(rn, cn, t + 1)]
                    seen[rn][cn] = True
    return -1


ans1 = run_bfs(BYTES_PART_1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

lo, hi = BYTES_PART_1, len(byte_pos)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    r = run_bfs(mid)
    if r == -1:
        hi = mid
    else:
        lo = mid

ans2 = ",".join(map(str, byte_pos[hi - 1]))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

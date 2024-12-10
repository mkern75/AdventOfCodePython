from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day10.txt"
grid = [list(map(int, list(line.rstrip("\n")))) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

reachable = [[set() for _ in range(C)] for _ in range(R)]
cnt = [[0 for _ in range(C)] for _ in range(R)]

ans1, ans2 = 0, 0
for n in range(9, -1, -1):
    for r in range(R):
        for c in range(C):
            if grid[r][c] != n:
                continue
            if grid[r][c] == 9:
                reachable[r][c] = {(r, c)}
                cnt[r][c] = 1
            else:
                for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= rn < R and 0 <= cn < C:
                        if grid[rn][cn] == grid[r][c] + 1:
                            reachable[r][c] |= reachable[rn][cn]
                            cnt[r][c] += cnt[rn][cn]
            if grid[r][c] == 0:
                ans1 += len(reachable[r][c])
                ans2 += cnt[r][c]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

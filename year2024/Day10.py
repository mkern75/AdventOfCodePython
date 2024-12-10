from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day10.txt"
grid = [list(map(int, list(line.rstrip("\n")))) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

pos = [[] for _ in range(10)]
for r in range(R):
    for c in range(C):
        pos[grid[r][c]].append((r, c))

peaks_reachable = [[set() for _ in range(C)] for _ in range(R)]
n_trails = [[0 for _ in range(C)] for _ in range(R)]

for height in range(9, 0, -1):
    for r, c in pos[height]:
        if height == 9:
            peaks_reachable[r][c] = {(r, c)}
            n_trails[r][c] = 1
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] == height - 1:
                peaks_reachable[rn][cn] |= peaks_reachable[r][c]
                n_trails[rn][cn] += n_trails[r][c]

ans1 = sum(len(peaks_reachable[r][c]) for r, c in pos[0])
ans2 = sum(n_trails[r][c] for r, c in pos[0])

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

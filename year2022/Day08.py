INPUT_FILE = "./year2022/data/day08.txt"
grid = [[int(c) for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        visible = all(grid[r][cn] < grid[r][c] for cn in range(0, c))
        visible |= all(grid[r][cn] < grid[r][c] for cn in range(c + 1, C))
        visible |= all(grid[rn][c] < grid[r][c] for rn in range(0, r))
        visible |= all(grid[rn][c] < grid[r][c] for rn in range(r + 1, R))
        ans1 += int(visible)
        score = next((c - cn for cn in range(c - 1, -1, -1) if grid[r][cn] >= grid[r][c]), c)
        score *= next((cn - c for cn in range(c + 1, C) if grid[r][cn] >= grid[r][c]), C - 1 - c)
        score *= next((r - rn for rn in range(r - 1, -1, -1) if grid[rn][c] >= grid[r][c]), r)
        score *= next((rn - r for rn in range(r + 1, R) if grid[rn][c] >= grid[r][c]), R - 1 - r)
        ans2 = max(ans2, score)
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

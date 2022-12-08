INPUT_FILE = "./year2022/data/day08.txt"
grid = [[int(c) for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        visible = not any(grid[r][cc] >= grid[r][c] for cc in range(0, c))
        visible |= not any(grid[r][cc] >= grid[r][c] for cc in range(c + 1, C))
        visible |= not any(grid[rr][c] >= grid[r][c] for rr in range(0, r))
        visible |= not any(grid[rr][c] >= grid[r][c] for rr in range(r + 1, R))
        ans1 += int(visible)
        score = abs(c - next((cc for cc in range(c - 1, -1, -1) if grid[r][cc] >= grid[r][c]), 0))
        score *= abs(c - next((cc for cc in range(c + 1, C) if grid[r][cc] >= grid[r][c]), C - 1))
        score *= abs(r - next((rr for rr in range(r - 1, -1, -1) if grid[rr][c] >= grid[r][c]), 0))
        score *= abs(r - next((rr for rr in range(r + 1, R) if grid[rr][c] >= grid[r][c]), R - 1))
        ans2 = max(ans2, score)
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

INPUT_FILE = "./year2022/data/day08.txt"
grid = [[int(c) for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        # part 1
        visible = sum(1 for cc in range(0, c) if grid[r][cc] >= grid[r][c]) == 0
        visible |= sum(1 for cc in range(c + 1, C) if grid[r][cc] >= grid[r][c]) == 0
        visible |= sum(1 for rr in range(0, r) if grid[rr][c] >= grid[r][c]) == 0
        visible |= sum(1 for rr in range(r + 1, R) if grid[rr][c] >= grid[r][c]) == 0
        ans1 += int(visible)
        # part 2
        s = abs(c - next((cc for cc in range(c - 1, -1, -1) if grid[r][cc] >= grid[r][c]), 0))
        s *= abs(c - next((cc for cc in range(c + 1, C) if grid[r][cc] >= grid[r][c]), C - 1))
        s *= abs(r - next((rr for rr in range(r - 1, -1, -1) if grid[rr][c] >= grid[r][c]), 0))
        s *= abs(r - next((rr for rr in range(r + 1, R) if grid[rr][c] >= grid[r][c]), R - 1))
        ans2 = max(ans2, s)
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

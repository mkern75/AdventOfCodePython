from time import time

time_start = time()
INPUT_FILE = "./year2025/data/day04.txt"

grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
n_rows, n_cols = len(grid), len(grid[0])


def neighbours8(r, c, n_rows, n_cols):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
                   (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
        if 0 <= rn < n_rows and 0 <= cn < n_cols:
            yield rn, cn


def get_accessible_rolls():
    accessible = []
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == "@":
                cnt = sum(1 for rn, cn in neighbours8(r, c, n_rows, n_cols) if grid[rn][cn] == "@")
                if cnt < 4:
                    accessible.append((r, c))
    return accessible


ans1 = len(get_accessible_rolls())
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
while True:
    to_remove = get_accessible_rolls()
    if not to_remove:
        break
    ans2 += len(to_remove)
    for r, c in to_remove:
        grid[r][c] = "."
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

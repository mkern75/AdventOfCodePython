from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day12.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]

N4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def regions(grid):
    rows, cols = len(grid), len(grid[0])
    seen = [[False] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            if not seen[r][c]:
                seen[r][c] = True
                region = {(r, c)}
                stack = [(r, c)]
                while stack:
                    rr, cc = stack.pop()
                    for dr, dc in N4:
                        rn, cn = rr + dr, cc + dc
                        if 0 <= rn < rows and 0 <= cn < cols and grid[rn][cn] == grid[rr][cc] and not seen[rn][cn]:
                            seen[rn][cn] = True
                            region.add((rn, cn))
                            stack.append((rn, cn))
                yield region


def area(region):
    return len(region)


def perimeter_1(region):
    p = 0
    for r, c in region:
        for dr, dc in N4:
            rn, cn = r + dr, c + dc
            if (rn, cn) not in region:
                p += 1
    return p


def perimeter_2(region):
    p = 0
    for r, c in region:
        for dr, dc in N4:
            rn, cn = r + dr, c + dc
            if (rn, cn) not in region:
                if r == rn and ((r - 1, cn) in region or (r - 1, c) not in region):
                    p += 1
                if c == cn and ((rn, c - 1) in region or (r, c - 1) not in region):
                    p += 1
    return p


ans1, ans2 = 0, 0
for region in regions(grid):
    ans1 += area(region) * perimeter_1(region)
    ans2 += area(region) * perimeter_2(region)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

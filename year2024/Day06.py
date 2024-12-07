from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day06.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

r_start, c_start = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "^")

r, c, dr, dc = r_start, c_start, -1, 0
seen_p1 = {(r_start, c_start)}
while True:
    while 0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] == "#":
        dr, dc = dc, -dr
    r, c = r + dr, c + dc
    if r < 0 or R <= r or c < 0 or C <= c:
        break
    seen_p1.add((r, c))

ans1 = len(seen_p1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def check_loop_p2():
    r, c, dr, dc = r_start, c_start, -1, 0
    seen = {hash((r_start, c_start, dr, dc))}
    while True:
        while 0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] == "#":
            dr, dc = dc, -dr
        r, c = r + dr, c + dc
        if r < 0 or R <= r or c < 0 or C <= c:
            return 0
        h = hash((r, c, dr, dc))
        if h in seen:
            return 1
        seen.add(h)


ans2 = 0
for r_obstr, c_obstr in seen_p1:
    if r_obstr == r_start and c_obstr == c_start:
        continue
    grid[r_obstr][c_obstr] = "#"
    ans2 += check_loop_p2()
    grid[r_obstr][c_obstr] = "."
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

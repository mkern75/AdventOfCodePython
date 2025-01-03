from time import time
from collections import defaultdict

time_start = time()
INPUT_FILE = "./year2024/data/day06.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
R, C = len(data), len(data[0])
grid = defaultdict(lambda: ".", {(r, c): v for r, row in enumerate(data) for c, v in enumerate(row)})

rs, cs = next((r, c) for r in range(R) for c in range(C) if grid[r, c] == "^")

r, c, dr, dc = rs, cs, -1, 0
seen_p1 = {(rs, cs)}
while True:
    while grid[r + dr, c + dc] == "#":
        dr, dc = dc, -dr
    r, c = r + dr, c + dc
    if r < 0 or R <= r or c < 0 or C <= c:
        break
    seen_p1.add((r, c))

ans1 = len(seen_p1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def simulate_p2(r_obstr, c_obstr):
    if r_obstr == rs and c_obstr == cs or grid[r_obstr, c_obstr] == "#":
        return 0
    r, c, dr, dc = rs, cs, -1, 0
    seen = {hash((rs, cs, dr, dc))}
    while True:
        while grid[r + dr, c + dc] == "#" or (r + dr == r_obstr and c + dc == c_obstr):
            dr, dc = dc, -dr
        r, c = r + dr, c + dc
        if r < 0 or R <= r or c < 0 or C <= c:
            return 0
        h = hash((r, c, dr, dc))
        if h in seen:
            return 1
        seen.add(h)


ans2 = sum(simulate_p2(r_obstr, c_obstr) for r_obstr, c_obstr in seen_p1)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

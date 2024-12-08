from time import time
from collections import defaultdict
from math import gcd

time_start = time()
INPUT_FILE = "./year2024/data/day08.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

antennas = defaultdict(list)
for r in range(R):
    for c in range(C):
        if grid[r][c] != ".":
            antennas[grid[r][c]] += [(r, c)]

antinodes_p1 = set()
antinodes_p2 = set()
for pos in antennas.values():
    n = len(pos)
    for i in range(n):
        for j in range(n):
            if i != j:
                r1, c1 = pos[i]
                r2, c2 = pos[j]
                dr = r1 - r2
                dc = c1 - c2
                if 0 <= r1 + dr < R and 0 <= c1 + dc < C:
                    antinodes_p1.add((r1 + dr, c1 + dc))
                g = gcd(dr, dc)
                dr //= g
                dc //= g
                k = 0
                while 0 <= r1 + k * dr < R and 0 <= c1 + k * dc < C:
                    antinodes_p2.add((r1 + k * dr, c1 + k * dc))
                    k += 1

ans1 = len(antinodes_p1)
ans2 = len(antinodes_p2)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

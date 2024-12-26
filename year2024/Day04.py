from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day04.txt"
g = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(g), len(g[0])


def valid(r, c):
    return 0 <= r and r < R and 0 <= c and c < C


ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        # part 1
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            if not valid(r + 3 * dr, c + 3 * dc):
                continue
            chr0 = g[r][c]
            chr1 = g[r + dr][c + dc]
            chr2 = g[r + 2 * dr][c + 2 * dc]
            chr3 = g[r + 3 * dr][c + 3 * dc]
            if chr0 == "X" and chr1 == "M" and chr2 == "A" and chr3 == "S":
                ans1 += 1
            if chr0 == "S" and chr1 == "A" and chr2 == "M" and chr3 == "X":
                ans1 += 1

        # part 2
        if g[r][c] != "A":
            continue
        if not valid(r - 1, c - 1) or not valid(r + 1, c + 1) or not valid(r - 1, c + 1) or not valid(r + 1, c - 1):
            continue
        chr1a = g[r - 1][c - 1]
        chr1b = g[r + 1][c + 1]
        if not ((chr1a == "M" and chr1b == "S") or (chr1a == "S" and chr1b == "M")):
            continue
        chr1a = g[r - 1][c + 1]
        chr1b = g[r + 1][c - 1]
        if not ((chr1a == "M" and chr1b == "S") or (chr1a == "S" and chr1b == "M")):
            continue
        ans2 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

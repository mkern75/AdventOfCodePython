from time import time
from collections import defaultdict

time_start = time()
INPUT_FILE = "./year2024/data/day04.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

R, C = len(data), len(data[0])
g = defaultdict(lambda: ".")
for r in range(R):
    for c in range(C):
        g[r, c] = data[r][c]

ans1, ans2 = 0, 0
for r in range(R):
    for c in range(C):
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            s = "".join(g[r + i * dr, c + i * dc] for i in range(4))
            if s == "XMAS" or s[::-1] == "XMAS":
                ans1 += 1
        s1 = "".join([g[r - 1, c - 1], g[r, c], g[r + 1, c + 1]])
        s2 = "".join([g[r - 1, c + 1], g[r, c], g[r + 1, c - 1]])
        if (s1 == "MAS" or s1[::-1] == "MAS") and (s2 == "MAS" or s2[::-1] == "MAS"):
            ans2 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day02.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
grid = [[int(c) for c in line.split()] for line in lines]

ans1 = 0
for row in grid:
    ans1 += max(row) - min(row)
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = 0
for row in grid:
    for a in row:
        for b in row:
            if a != b and a % b == 0:
                ans2 += a // b
    ans1 += max(row) - min(row)
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

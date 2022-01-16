from utils import load_int_grid

INPUT_FILE = "./year2017/data/day02.txt"

grid = load_int_grid(INPUT_FILE, "\t")

ans1 = 0
for row in grid:
    ans1 += max(row) - min(row)
print("part 1:", ans1)

ans2 = 0
for row in grid:
    for a in row:
        for b in row:
            if a != b and a % b == 0:
                ans2 += a // b
    ans1 += max(row) - min(row)
print("part 2:", ans2)

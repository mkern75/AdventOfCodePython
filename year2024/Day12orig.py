from time import time
from collections import defaultdict

time_start = time()
INPUT_FILE = "./year2024/data/day12.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
R, C = len(data), len(data[0])
grid = defaultdict(lambda: ".", {(r, c): v for r, row in enumerate(data) for c, v in enumerate(row)})

ans1, ans2 = 0, 0
seen = set()

for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue

        stack = [(r, c)]
        seen |= {(r, c)}
        region = {(r, c)}
        while stack:
            rr, cc = stack.pop()
            for rn, cn in [(rr + 1, cc), (rr - 1, cc), (rr, cc + 1), (rr, cc - 1)]:
                if grid[rn, cn] == grid[rr, cc] and not (rn, cn) in seen:
                    stack += [(rn, cn)]
                    seen |= {(rn, cn)}
                    region |= {(rn, cn)}

        area = len(region)

        perimeter_1 = 0
        for rr, cc in region:
            for rn, cn in [(rr + 1, cc), (rr - 1, cc), (rr, cc + 1), (rr, cc - 1)]:
                if (rn, cn) not in region:
                    perimeter_1 += 1

        perimeter_2 = 0
        for rr, cc in region:
            if (rr, cc - 1) not in region and ((rr - 1, cc) not in region or (rr - 1, cc - 1) in region):
                perimeter_2 += 1
            if (rr, cc + 1) not in region and ((rr - 1, cc) not in region or (rr - 1, cc + 1) in region):
                perimeter_2 += 1
            if (rr - 1, cc) not in region and ((rr, cc - 1) not in region or (rr - 1, cc - 1) in region):
                perimeter_2 += 1
            if (rr + 1, cc) not in region and ((rr, cc - 1) not in region or (rr + 1, cc - 1) in region):
                perimeter_2 += 1

        ans1 += area * perimeter_1
        ans2 += area * perimeter_2

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

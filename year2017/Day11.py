import time

# see https://www.redblobgames.com/grids/hexagons/ for axial coordinates
# my x-axis: n (+) to s (-) / y-axis: nw (+) to se (-)
AXIAL = {"n": (1, 0), "s": (-1, 0), "nw": (0, 1), "se": (0, -1), "ne": (1, -1), "sw": (-1, 1)}

t0 = time.time()
INPUT_FILE = "./year2017/data/day11.txt"


def move(x, y, d):
    dx, dy = AXIAL[d]
    return x + dx, y + dy


def dist(x, y):
    return abs(x) + abs(y) if x * y >= 0 else max(abs(x), abs(y))


file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

directions = lines[0].split(",")

x, y, max_steps = 0, 0, 0
for d in directions:
    x, y = move(x, y, d)
    max_steps = max(max_steps, dist(x, y))

ans1 = dist(x, y)
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = max_steps
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

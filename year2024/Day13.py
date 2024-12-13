from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day13.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


# Find non-nengative integers a, b such that
#   a * x[0] + b * x[1] = x[2]
#   a * y[0] + b * y[1] = y[2]
def solve(x, y):
    cc = x[2] * y[0] - y[2] * x[0]
    bb = x[1] * y[0] - y[1] * x[0]
    if cc % bb != 0:
        return tuple()
    b = cc // bb
    if (x[2] - b * x[1]) % x[0] != 0:
        return tuple()
    a = (x[2] - b * x[1]) // x[0]
    if a >= 0 and b >= 0:
        return a, b
    return tuple()


ans1, ans2 = 0, 0
for block in blocks:
    x, y = [0] * 3, [0] * 3
    for i in range(3):
        _, right = block[i].split(": ")
        xs, ys = right.split(", ")
        x[i], y[i] = int(xs[2:]), int(ys[2:])

    res = solve(x, y)
    if res:
        ans1 += 3 * res[0] + res[1]

    x[2] += 10000000000000
    y[2] += 10000000000000
    res = solve(x, y)
    if res:
        ans2 += 3 * res[0] + res[1]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

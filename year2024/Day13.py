from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day13.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


# Find non-nengative integers x, y such that:
#   x * a[0] + y * b[0] = c[0]
#   x * a[1] + y * b[1] = c[1]
def solve(a, b, c):
    cc = c[0] * a[1] - c[1] * a[0]
    bb = b[0] * a[1] - b[1] * a[0]
    if cc % bb != 0:
        return tuple()
    y = cc // bb
    if (c[0] - y * b[0]) % a[0] != 0:
        return tuple()
    x = (c[0] - y * b[0]) // a[0]
    if x >= 0 and y >= 0:
        return x, y
    return tuple()


def nums(input_line):
    return list(map(lambda s: int(s[2:]), input_line.split(": ")[1].split(", ")))


ans1, ans2 = 0, 0
for block in blocks:
    a = nums(block[0])
    b = nums(block[1])
    c = nums(block[2])

    res = solve(a, b, c)
    if res:
        ans1 += 3 * res[0] + res[1]

    c = [v + 10000000000000 for v in c]
    res = solve(a, b, c)
    if res:
        ans2 += 3 * res[0] + res[1]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

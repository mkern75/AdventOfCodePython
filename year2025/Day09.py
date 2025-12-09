from time import time

time_start = time()


class CoordinateCompression:
    def __init__(self, original_values, n_bits=32):
        import random
        self._rand_bits = random.getrandbits(n_bits)  # anti-hacking!
        self._orig_vals = []
        self._map = {}
        for x in sorted(original_values):
            if not self._orig_vals or x != self._orig_vals[-1]:
                self._orig_vals += [x]
                self._map[x ^ self._rand_bits] = len(self._map)
        self.n = len(self._orig_vals)

    def compressed_value(self, original_value):
        return self._map[original_value ^ self._rand_bits]

    def original_value(self, compressed_value):
        return self._orig_vals[compressed_value]

    def n_compressed_values(self):
        return self.n


INPUT_FILE = "./year2025/data/day09.txt"

data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
p = [tuple(map(int, line.split(","))) for line in data]
n = len(p)

ans1 = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        dx = abs(p[i][0] - p[j][0])
        dy = abs(p[i][1] - p[j][1])
        ans1 = max(ans1, (dx + 1) * (dy + 1))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# coordinate compression
x_values, y_values = set(), set()
for x, y in p:
    x_values |= {x - 1, x, x + 1}
    y_values |= {y - 1, y, y + 1}
x_compression = CoordinateCompression(x_values)
y_compression = CoordinateCompression(y_values)
pp = [(x_compression.compressed_value(x), y_compression.compressed_value(y)) for x, y in p]

# build set of coordinates that are inside the area
inside = set()

# walk along the perimeter
for i in range(n):
    x1, y1 = pp[i]
    x2, y2 = pp[(i + 1) % n]
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            inside.add((x, y))

# fill inside
x_max = max(x for x, _ in pp)
i1 = next(i for i in range(n) if pp[i][0] == x_max)
i2 = (i1 + 1) % n if pp[(i1 + 1) % n][0] == x_max else (i1 - 1) % n
if pp[i1][1] < pp[i2][1]:
    q = [(pp[i1][0] - 1, pp[i1][1] + 1)]
else:
    q = [(pp[i1][0] - 1, pp[[i1][1] - 1])]
assert q[0] not in inside
inside.add((q[0]))
for x, y in q:
    for xn, yn in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (xn, yn) not in inside:
            inside.add((xn, yn))
            q.append((xn, yn))


def check_inside(x1, y1, x2, y2):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if (x1, y) not in inside:
            return False
        if (x2, y) not in inside:
            return False
    for x in range(min(x1, x2), max(x1, x2 + 1) + 1):
        if (x, y1) not in inside:
            return False
        if (x, y2) not in inside:
            return False
    return True


ans2 = 0
for i in range(n - 1):
    x1, y1 = pp[i][0], pp[i][1]
    for j in range(i + 1, n):
        x2, y2 = pp[j][0], pp[j][1]
        if check_inside(x1, y1, x2, y2):
            dx = abs(x_compression.original_value(x2) - x_compression.original_value(x1))
            dy = abs(y_compression.original_value(y2) - y_compression.original_value(y1))
            ans2 = max(ans2, (dx + 1) * (dy + 1))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

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


INPUT_FILE = "./year2025/data/day05.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

id_ranges = [tuple(map(int, line.split("-"))) for line in blocks[0]]

ans1 = sum(any(x <= int(line) <= y for x, y in id_ranges) for line in blocks[1])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

vals = []
for x, y in id_ranges:
    vals.extend([x, y + 1])
cc = CoordinateCompression(vals)
id_ranges_compressed = [(cc.compressed_value(x), cc.compressed_value(y + 1)) for x, y in id_ranges]

ans2 = 0
for i in range(cc.n_compressed_values()):
    if any(x <= i < y for x, y in id_ranges_compressed):
        ans2 += cc.original_value(i + 1) - cc.original_value(i)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

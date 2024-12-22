from time import time
from collections import Counter

time_start = time()

INPUT_FILE = "./year2024/data/day22.txt"
numbers = [int(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]

MOD = 16777216
N = 2_000


def update(x):
    x = (x ^ (x << 6)) % MOD
    x = (x ^ (x >> 5)) % MOD
    x = (x ^ (x << 11)) % MOD
    return x


x = [0] * (N + 1)  # secret numbers
b = [0] * (N + 1)  # prices
d = [0] * (N + 1)  # deltas
res = Counter()

ans1 = 0
for buyer_id, secret_number in enumerate(numbers, start=1):
    x[0] = secret_number
    b[0] = x[0] % 10
    for i in range(1, N + 1):
        x[i] = update(x[i - 1])
        b[i] = x[i] % 10
        d[i] = b[i] - b[i - 1]

    ans1 += x[N]

    seen = set()
    for i in range(4, N + 1):
        h = tuple(d[i - 3:i + 1])
        if h not in seen:
            seen.add(h)
            res[h] += b[i]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = max(res.values())
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

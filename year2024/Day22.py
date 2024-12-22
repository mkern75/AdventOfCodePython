from time import time

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
seen = [0] * (1 << 20)
res = [0] * (1 << 20)

ans1 = 0
for buyer_id, secret_number in enumerate(numbers, start=1):
    x[0] = secret_number
    b[0] = x[0] % 10
    for i in range(1, N + 1):
        x[i] = update(x[i - 1])
        b[i] = x[i] % 10
        d[i] = b[i] - b[i - 1]

    ans1 += x[N]

    # Each change is between -9 and +9.
    # By adding 9, this range becomes 0 to +18 which fits into 5 bits.
    # This allows us to map each possible tuple of 4 changes onto a distict index between 0 and 2**20.
    # This significantly speeds the calculations up (tuples are slow).
    for i in range(4, N + 1):
        h = ((d[i - 3] + 9) << 15) | ((d[i - 2] + 9) << 10) | ((d[i - 1] + 9) << 5) | (d[i] + 9)
        if seen[h] != buyer_id:
            seen[h] = buyer_id
            res[h] += b[i]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = max(res)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

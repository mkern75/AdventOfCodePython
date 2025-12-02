from time import time

time_start = time()


def is_invalid(x: int, repeats: int) -> bool:
    s = str(x)
    if len(s) % repeats != 0:
        return False
    k = len(s) // repeats
    for i in range(1, repeats):
        if s[i * k:(i * k + k)] != s[:k]:
            return False
    return True


INPUT_FILE = "./year2025/data/day02.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

for rng in data[0].split(","):
    lo, hi = map(int, rng.split("-"))
    for x in range(lo, hi + 1):
        if is_invalid(x, 2):
            ans1 += x
        if any(is_invalid(x, r) for r in range(2, len(str(x)) + 1)):
            ans2 += x

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

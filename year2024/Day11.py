from time import time
from functools import cache

time_start = time()
INPUT_FILE = "./year2024/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


@cache
def solve(num, blinks):
    if blinks == 0:
        return 1

    if num == 0:
        return solve(1, blinks - 1)

    s = str(num)
    k = len(s)
    if k & 1 == 0:
        h = k >> 1
        return solve(int(s[:h]), blinks - 1) + solve(int(s[h:]), blinks - 1)

    return solve(num * 2024, blinks - 1)


nums = list(map(int, data[0].split()))

ans1 = sum(solve(num, 25) for num in nums)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = sum(solve(num, 75) for num in nums)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

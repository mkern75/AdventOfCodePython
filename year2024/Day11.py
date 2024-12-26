from time import time
from collections import Counter
from functools import cache

time_start = time()
INPUT_FILE = "./year2024/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


@cache
def replacement(n):
    if n == 0:
        return (1,)
    s = str(n)
    k = len(s)
    if k & 1 == 0:
        h = k >> 1
        return int(s[:h]), int(s[h:])
    return (2024 * n,)


def solve(nums, blinks):
    cnt = Counter(nums)
    for _ in range(blinks):
        cnt_new = Counter()
        for n, c in cnt.items():
            for m in replacement(n):
                cnt_new[m] += c
        cnt = cnt_new
    return sum(cnt.values())

    #
    # if blinks == 0:
    #     return 1
    #
    # if num == 0:
    #     return solve(1, blinks - 1)
    #
    # s = str(num)
    # k = len(s)
    # if k & 1 == 0:
    #     h = k >> 1
    #     return solve(int(s[:h]), blinks - 1) + solve(int(s[h:]), blinks - 1)
    #
    # return solve(num * 2024, blinks - 1)


nums = list(map(int, data[0].split()))

ans1 = solve(nums, 25)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = solve(nums, 75)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

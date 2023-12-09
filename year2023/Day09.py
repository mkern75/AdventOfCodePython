INPUT_FILE = "./year2023/data/day09.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


def extrapolate(a: list[int]) -> int:
    res = 0
    while any(x for x in a):
        res += a[-1]
        a = [y - x for x, y in zip(a, a[1:])]
    return res


ans1, ans2 = 0, 0

for line in data:
    nums = list(map(int, line.split()))
    ans1 += extrapolate(nums)
    ans2 += extrapolate(nums[::-1])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

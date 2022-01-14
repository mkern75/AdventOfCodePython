from utils import load_numbers, tic, toc

INPUT_FILE = "./year2019/data/day04.txt"


def digits(n):
    if n == 0:
        return []
    return digits(n // 10) + [n % 10]


def valid_password(n, exactly_two=False):
    d = digits(n)
    same_digits, no_decrease = False, True
    for i in range(len(d) - 1):
        if d[i] == d[i + 1]:
            if exactly_two:
                if (i == 0 or d[i - 1] != d[i]) and (i + 2 >= len(d) or d[i + 1] != d[i + 2]):
                    same_digits = True
            else:
                same_digits = True
        if d[i] > d[i + 1]:
            no_decrease = False
    return len(d) == 6 and same_digits and no_decrease


tic()
low, high = load_numbers(INPUT_FILE, "-")
ans1 = 0
for n in range(low, high + 1):
    if valid_password(n):
        ans1 += 1
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
ans2 = 0
for n in range(low, high + 1):
    if valid_password(n, True):
        ans2 += 1
print(f"part 2: {ans2}   ({toc():.3f}s)")

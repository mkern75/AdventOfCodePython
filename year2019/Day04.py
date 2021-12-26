from datetime import datetime

file = open("./year2019/data/day04.txt", "r")
lines = [line.rstrip('\n') for line in file]


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


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

low, high = map(int, lines[0].split("-"))
ans1, ans2 = 0, 0
for n in range(low, high + 1):
    if valid_password(n):
        ans1 += 1
    if valid_password(n, True):
        ans2 += 1
print("part 1:", ans1)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

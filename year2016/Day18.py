from datetime import datetime

INPUT_FILE = "./year2016/data/day18.txt"


def n_safe(row):
    return row.count(".")


def is_trap(row, i):
    return row[i] == "^" if 0 <= i < len(row) else False


def next(row):
    next_row = ""
    for i in range(len(row)):
        if is_trap(row, i - 1) and is_trap(row, i) and not is_trap(row, i + 1):
            next_row += "^"
        elif not is_trap(row, i - 1) and is_trap(row, i) and is_trap(row, i + 1):
            next_row += "^"
        elif is_trap(row, i - 1) and not is_trap(row, i) and not is_trap(row, i + 1):
            next_row += "^"
        elif not is_trap(row, i - 1) and not is_trap(row, i) and is_trap(row, i + 1):
            next_row += "^"
        else:
            next_row += "."
    return next_row


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

row = lines[0]
ans1 = 0
for i in range(40):
    ans1 += n_safe(row)
    row = next(row)
print("part 1:", ans1)

row = lines[0]
ans2 = 0
for i in range(400000):
    ans2 += n_safe(row)
    row = next(row)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

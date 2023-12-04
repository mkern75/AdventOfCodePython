INPUT_FILE = "./year2023/data/day01.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIGITS_SPELLED = list("one, two, three, four, five, six, seven, eight, nine".split(", "))

ans1, ans2 = 0, 0
for line in data:
    digits1, digits2 = [], []
    for i, c in enumerate(line):
        if c.isdigit():
            digits1 += [int(c)]
            digits2 += [int(c)]
        for d, digit_spelled in enumerate(DIGITS_SPELLED, 1):
            if line[i:].startswith(digit_spelled):
                digits2 += [d]
    ans1 += 10 * digits1[0] + digits1[-1]
    ans2 += 10 * digits2[0] + digits2[-1]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

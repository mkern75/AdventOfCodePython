INPUT_FILE = "./year2023/data/day01.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

DIGITS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
DIGITS_PLUS = DIGITS | {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                        "eight": 8, "nine": 9}


def first_digit(s, digits):
    for i in range(len(s)):
        for d in digits.keys():
            if s[i:].startswith(d):
                return digits[d]


def last_digit(s, digits):
    for i in range(len(s) - 1, -1, -1):
        for d in digits.keys():
            if s[i:].startswith(d):
                return digits[d]


ans1, ans2 = 0, 0
for line in data:
    ans1 += 10 * first_digit(line, DIGITS) + last_digit(line, DIGITS)
for line in data:
    ans2 += 10 * first_digit(line, DIGITS_PLUS) + last_digit(line, DIGITS_PLUS)

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

from utils import load_word

INPUT_FILE = "./year2017/data/day01.txt"

digits = [int(c) for c in load_word(INPUT_FILE)]

ans1 = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + 1) % len(digits)]:
        ans1 += digits[i]
print("part 1:", ans1)

ans2 = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + len(digits) // 2) % len(digits)]:
        ans2 += digits[i]
print("part 2:", ans2)

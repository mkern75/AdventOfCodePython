import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day01.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
digits = [int(c) for c in lines[0]]

ans1 = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + 1) % len(digits)]:
        ans1 += digits[i]
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")

ans2 = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + len(digits) // 2) % len(digits)]:
        ans2 += digits[i]
print("part 2:", ans2, f"  ({time.time() - t0:.3f}s)")

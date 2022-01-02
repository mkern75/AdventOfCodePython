import re
import time

t0 = time.time()
INPUT_FILE = "./year2020/data/day02.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

ans1 = 0
for line in lines:
    m = re.compile(r"([0-9]+)-([0-9]+) ([a-z]+): (.*)").match(line)
    low, high, c, pw = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    if low <= pw.count(c) <= high:
        ans1 += 1
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = 0
for line in lines:
    m = re.compile(r"([0-9]+)-([0-9]+) ([a-z]+): (.*)").match(line)
    low, high, c, pw = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    if (pw[low - 1] == c and pw[high - 1] != c) or (pw[low - 1] != c and pw[high - 1] == c):
        ans2 += 1
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

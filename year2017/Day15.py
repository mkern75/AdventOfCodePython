from utils import load_lines, tic, toc

INPUT_FILE = "./year2017/data/day15.txt"

tic()
lines = load_lines(INPUT_FILE)

a = int(lines[0].split()[4])
b = int(lines[1].split()[4])

ans1 = 0
for i in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a % 65536 == b % 65536:
        ans1 += 1
print(f"part 1: {ans1}  ({toc():.3f}s)")

tic()
a = int(lines[0].split()[4])
b = int(lines[1].split()[4])

ans2 = 0
for i in range(5000000):
    a = (a * 16807) % 2147483647
    while a % 4 != 0:
        a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while b % 8 != 0:
        b = (b * 48271) % 2147483647
    if a % 65536 == b % 65536:
        ans2 += 1
print(f"part 2: {ans2}  ({toc():.3f}s)")

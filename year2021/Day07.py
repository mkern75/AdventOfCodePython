import sys

file = open("./data/year2021/day07.txt", "r")
lines = [line.rstrip('\n') for line in file]
p = [int(_) for _ in lines[0].split(",")]

fb1, fb2 = sys.maxsize, sys.maxsize
for m in range(min(p), max(p) + 1):
    f1, f2 = 0, 0
    for i in p:
        f1 += abs(m - i)
        f2 += abs(m - i) * (abs(m - i) + 1) // 2
    fb1 = min(fb1, f1)
    fb2 = min(fb2, f2)
print(fb1)
print(fb2)

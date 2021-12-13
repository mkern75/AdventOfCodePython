import numpy as np

file = open("./year2015/data/day06.txt", "r")
lines = [line.rstrip('\n') for line in file]

L1 = np.zeros((1000, 1000), dtype=int)
L2 = np.zeros((1000, 1000), dtype=int)
for line in lines:
    s = line.split()
    x1, y1 = map(int, s[-3].split(","))
    x2, y2 = map(int, s[-1].split(","))
    if line.startswith("turn on"):
        L1[x1:x2 + 1, y1:y2 + 1] = 1
        L2[x1:x2 + 1, y1:y2 + 1] += 1
    elif line.startswith("turn off"):
        L1[x1:x2 + 1, y1:y2 + 1] = 0
        L2[x1:x2 + 1, y1:y2 + 1] -= 1
        L2[L2 < 0] = 0
    if line.startswith("toggle"):
        L1[x1:x2 + 1, y1:y2 + 1] = 1 - L1[x1:x2 + 1, y1:y2 + 1]
        L2[x1:x2 + 1, y1:y2 + 1] += 2
print(np.sum(L1))
print(np.sum(L2))

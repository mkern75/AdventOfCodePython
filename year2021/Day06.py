import numpy as np

file = open("./year2021/data/day06.txt", "r")
lines = [line.rstrip('\n') for line in file]
fish = [int(f) for f in lines[0].split(",")]

c = np.zeros((257, 9), dtype=int)

for i in range(len(fish)):
    c[0][fish[i]] += 1
for d in range(1, 257):
    for i in range(0, 8):
        c[d][i] = c[d - 1][i + 1]
    c[d][8] = c[d - 1][0]
    c[d][6] += c[d - 1][0]
print(sum(c[80]))
print(sum(c[256]))

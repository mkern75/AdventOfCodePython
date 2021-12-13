file = open("./year2021/data/day01.txt", "r")
depth = [int(line.rstrip('\n')) for line in file]
n = len(depth)

a, b = 0, 0
for i in range(1, n):
    if depth[i] > depth[i - 1]:
        a += 1
for i in range(3, n):
    if depth[i] > depth[i - 3]:
        b += 1
print(a)
print(b)

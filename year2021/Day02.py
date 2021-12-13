file = open("./year2021/data/day02.txt", "r")
lines = [line.rstrip('\n').split(" ") for line in file]

h1, d1 = 0, 0
h2, d2, a2 = 0, 0, 0
for line in lines:
    if line[0] == "forward":
        h1 += int(line[1])
        h2 += int(line[1])
        d2 += a2 * int(line[1])
    elif line[0] == "down":
        d1 += int(line[1])
        a2 += int(line[1])
    elif line[0] == "up":
        d1 -= int(line[1])
        a2 -= int(line[1])
print(h1 * d1)
print(h2 * d2)

file = open("./year2015/data/day08.txt", "r")
lines = [line.rstrip('\n') for line in file]

delta = 0
for line in lines:
    delta += len(line)
    pos = 1
    while pos < len(line) - 1:
        delta -= 1
        if line[pos] == "\\" and line[pos + 1] == "x":
            pos += 4
        elif line[pos] == "\\":
            pos += 2
        else:
            pos += 1
print(delta)

delta = 0
for line in lines:
    delta += 2 + line.count("\\") + line.count("\"")
print(delta)
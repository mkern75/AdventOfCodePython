file = open("./year2015/data/day01.txt", "r")
lines = [line.rstrip('\n') for line in file]

floor, pos, basement = 0, 0, 0
for line in lines:
    for c in line:
        if c in ["(", ")"]:
            floor += 1 if c == "(" else -1
            pos += 1
        if basement == 0 and floor < 0:
            basement = pos
print(floor)
print(basement)

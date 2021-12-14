file = open("./year2015/data/day25.txt", "r")
lines = [line.rstrip('\n') for line in file]

s = lines[0].split()
tr = int(s[15].strip(","))  # target row
tc = int(s[17].strip("."))  # target column
r, c = 1, 1

x = 20151125
while r != tr or c != tc:
    x = (x * 252533) % 33554393
    if r == 1:
        r, c = c + 1, 1
    else:
        r, c = r - 1, c + 1
print(x)

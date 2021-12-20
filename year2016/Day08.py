file = open("./year2016/data/day08.txt", "r")
lines = [line.rstrip('\n') for line in file]


def rect(d, x, y):
    for r in range(y):
        for c in range(x):
            d[r][c] = True


def rotate_col(d, x, a):
    h = len(d)
    col = [False] * h
    for r in range(h):
        col[(r + a) % h] = d[r][x]
    for r in range(h):
        d[r][x] = col[r]


def rotate_row(d, y, a):
    w = len(d[0])
    row = [False] * w
    for c in range(w):
        row[(c + a) % w] = d[y][c]
    for c in range(w):
        d[y][c] = row[c]


def count(d):
    return sum(sum(r) for r in d)


def display(d):
    for r in range(len(d)):
        for c in range(len(d[0])):
            print("#" if d[r][c] else ".", end="")
        print()


W = 50
H = 6
D = [[False for i in range(W)] for j in range(H)]

for instr in lines:
    if instr.startswith("rect"):
        a, b = list(map(int, instr[5:].split("x")))
        rect(D, a, b)
    elif instr.startswith("rotate column"):
        a, b = list(map(int, instr[16:].split(" by ")))
        rotate_col(D, a, b)
    elif instr.startswith("rotate row"):
        a, b = list(map(int, instr[13:].split(" by ")))
        rotate_row(D, a, b)
print("part 1:", count(D))

print("part 2:")
display(D)

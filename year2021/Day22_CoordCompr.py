import numpy as np
from math import inf
from datetime import datetime

INPUT_FILE = "./year2021/data/day22.txt"


def parse_input(lines):
    instructions = []
    for line in lines:
        cmd, tmp = line.split(" ")
        x, y, z = tmp.split(",")
        x0, x1 = list(map(int, x[2:].split("..")))
        y0, y1 = list(map(int, y[2:].split("..")))
        z0, z1 = list(map(int, z[2:].split("..")))
        instructions += [(cmd, (x0, x1, y0, y1, z0, z1))]
    return instructions


def index(x, X):
    i = 0
    while i + 1 < len(X) and x >= X[i + 1]:
        i += 1
    return i


def compress_coord(c, X, Y, Z):
    return index(c[0], X), index(c[1], X), index(c[2], Y), index(c[3], Y), index(c[4], Z), index(c[5], Z)


def count_cubes(C, X, Y, Z):
    cnt = 0
    idx = np.where(C == True)
    for i in range(len(idx[0])):
        x, y, z = idx[0][i], idx[1][i], idx[2][i]
        cnt += (X[x + 1] - X[x]) * (Y[y + 1] - Y[y]) * (Z[z + 1] - Z[z])
    return cnt


# adjusts a cuboid c to its overlap with limited area (-lt, +lt, -lt, +lt, -lt, +lt)
def adjust(c, lt):
    if max([abs(c[i]) for i in range(6)]) > lt:
        return None
    return max(c[0], -lt), min(c[1], +lt), max(c[2], -lt), min(c[3], +lt), max(c[4], -lt), min(c[5], +lt)


# main idea: coordinate compression (though my other idea of maintaining list of non-overlapping cuboids is faster)
def solve(instructions, limit=inf):
    X, Y, Z = set(), set(), set()

    for instr in instructions:
        _, cuboid = instr
        cuboid = adjust(cuboid, limit)
        if cuboid is not None:
            X.update([cuboid[0], cuboid[1] + 1])
            Y.update([cuboid[2], cuboid[3] + 1])
            Z.update([cuboid[4], cuboid[5] + 1])

    X = sorted(list(X))
    Y = sorted(list(Y))
    Z = sorted(list(Z))

    N = max(len(X), len(Y), len(Z))
    C = np.zeros((N, N, N), dtype=bool)

    for instr in instructions:
        cmd, cuboid = instr
        cuboid = adjust(cuboid, limit)
        if cuboid is not None:
            cuboid = compress_coord(cuboid, X, Y, Z)
            if cmd == "on":
                C[cuboid[0]:cuboid[1] + 1, cuboid[2]:cuboid[3] + 1, cuboid[4]:cuboid[5] + 1] = True
            elif cmd == "off":
                C[cuboid[0]:cuboid[1] + 1, cuboid[2]:cuboid[3] + 1, cuboid[4]:cuboid[5] + 1] = False

    return count_cubes(C, X, Y, Z)


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
instructions = parse_input(lines)
print("part 1:", solve(instructions, 50))
print("part 2:", solve(instructions))

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

import numpy as np
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


def filter_instructions_part_1(instructions):
    filtered_instructions = []
    for instr in instructions:
        _, (x0, x1, y0, y1, z0, z1) = instr
        if max([abs(x0), abs(x1), abs(y0), abs(y1), abs(z0), abs(z1)]) <= 50:
            filtered_instructions += [instr]
    return filtered_instructions


def index(x, X):
    i = 0
    while i + 1 < len(X) and x >= X[i + 1]:
        i += 1
    return i


def compress_coord(x0, x1, y0, y1, z0, z1, X, Y, Z):
    return index(x0, X), index(x1, X), index(y0, Y), index(y1, Y), index(z0, Z), index(z1, Z),


def count_cubes(C, X, Y, Z):
    cnt = 0
    idx = np.where(C == True)
    for i in range(len(idx[0])):
        x, y, z = idx[0][i], idx[1][i], idx[2][i]
        cnt += (X[x + 1] - X[x]) * (Y[y + 1] - Y[y]) * (Z[z + 1] - Z[z])
    return cnt


# main idea: coordinate compression (though my other idea of maintaining list of non-overlapping cuboids is faster)
def solve(instructions):
    X, Y, Z = set(), set(), set()

    for instr in instructions:
        _, (x0, x1, y0, y1, z0, z1) = instr
        X.update([x0, x1 + 1])
        Y.update([y0, y1 + 1])
        Z.update([z0, z1 + 1])

    X = sorted(list(X))
    Y = sorted(list(Y))
    Z = sorted(list(Z))

    N = max(len(X), len(Y), len(Z))
    C = np.zeros((N, N, N), dtype=bool)

    for instr in instructions:
        cmd, (x0, x1, y0, y1, z0, z1) = instr
        x0, x1, y0, y1, z0, z1 = compress_coord(x0, x1, y0, y1, z0, z1, X, Y, Z)
        if cmd == "on":
            C[x0:x1 + 1, y0:y1 + 1, z0:z1 + 1] = True
        elif cmd == "off":
            C[x0:x1 + 1, y0:y1 + 1, z0:z1 + 1] = False

    return count_cubes(C, X, Y, Z)


print("start:", datetime.now())

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
instructions = parse_input(lines)
print("part 1:", solve(filter_instructions_part_1(instructions)))
print("part 2:", solve(instructions))

print("finish:", datetime.now())

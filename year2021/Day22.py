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


def count(cuboid):
    return (cuboid[1] - cuboid[0] + 1) * (cuboid[3] - cuboid[2] + 1) * (cuboid[5] - cuboid[4] + 1)


def is_inside(c1, c2):
    if c1[0] >= c2[0] and c1[1] <= c2[1] and c1[2] >= c2[2] and c1[3] <= c2[3] and c1[4] >= c2[4] and c1[5] <= c2[5]:
        return True
    return False


def has_overlap(c1, c2):
    if c1[0] > c2[1] or c1[1] < c2[0] or c1[2] > c2[3] or c1[3] < c2[2] or c1[4] > c2[5] or c1[5] < c2[4]:
        return False
    return True


# returns a list of non-overlapping cuboids that represent cuboid c1 minus cuboid c2
def minus(c1, c2):
    if is_inside(c1, c2):
        return []
    elif not has_overlap(c1, c2):
        return [c1]
    else:
        x1, x2 = max(c1[0], c2[0]), min(c1[1], c2[1])
        y1, y2 = max(c1[2], c2[2]), min(c1[3], c2[3])
        z1, z2 = max(c1[4], c2[4]), min(c1[5], c2[5])
        lx = [(x1, x2)]
        if c1[0] < x1:
            lx += [(c1[0], x1 - 1)]
        if c1[1] > x2:
            lx += [(x2 + 1, c1[1])]
        ly = [(y1, y2)]
        if c1[2] < y1:
            ly += [(c1[2], y1 - 1)]
        if c1[3] > y2:
            ly += [(y2 + 1, c1[3])]
        lz = [(z1, z2)]
        if c1[4] < z1:
            lz += [(c1[4], z1 - 1)]
        if c1[5] > z2:
            lz += [(z2 + 1, c1[5])]
        res = []
        for x in lx:
            for y in ly:
                for z in lz:
                    res += [(x[0], x[1], y[0], y[1], z[0], z[1])]
        res.remove((x1, x2, y1, y2, z1, z2))
        return res


# takes a list of non-overlapping cuboids and adds another cuboid
# result is again a list of non-overlapping cuboids
def combine_add(list_of_cuboids, cuboid_to_add):
    result = []
    for c in list_of_cuboids:
        result += minus(c, cuboid_to_add)
    return result + [cuboid_to_add]


# takes a list of non-overlapping cuboids and removes a cuboid
# result is again a list of non-overlapping cuboids
def combine_remove(list_of_cuboids, cuboid_to_remove):
    result = []
    for c in list_of_cuboids:
        result += minus(c, cuboid_to_remove)
    return result


# adjusts a cuboid c to its overlap with limited area (-lt, +lt, -lt, +lt, -lt, +lt)
def adjust(c, lt):
    if max([abs(c[i]) for i in range(6)]) > lt:
        return None
    return max(c[0], -lt), min(c[1], +lt), max(c[2], -lt), min(c[3], +lt), max(c[4], -lt), min(c[5], +lt)


def solve(instructions, limit=inf):
    C = []  # list of non-overlapping cuboids
    for instr in instructions:
        cmd, cuboid = instr
        cuboid = adjust(cuboid, limit)
        if cuboid is not None:
            if cmd == "on":
                C = combine_add(C, cuboid)
            else:
                C = combine_remove(C, cuboid)
    return sum([count(c) for c in C])


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
instructions = parse_input(lines)
print("part 1:", solve(instructions, 50))
print("part 2:", solve(instructions))

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

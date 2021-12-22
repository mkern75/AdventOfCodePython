from datetime import datetime

file = open("./year2021/data/day22.txt", "r")
lines = [line.rstrip('\n') for line in file]


def parse_step(line):
    cmd, tmp = line.split(" ")
    x, y, z = tmp.split(",")
    x1, x2 = list(map(int, x[2:].split("..")))
    y1, y2 = list(map(int, y[2:].split("..")))
    z1, z2 = list(map(int, z[2:].split("..")))
    return cmd, (x1, x2, y1, y2, z1, z2)


def included_in_part_1(cuboid):
    for i in range(6):
        if cuboid[i] < -50 or 50 < cuboid[i]:
            return False
    return True


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
    if not list_of_cuboids:
        return [cuboid_to_add]
    to_add = [cuboid_to_add]
    for c in list_of_cuboids:
        new_to_add = []
        for x in to_add:
            new_to_add += minus(x, c)
        to_add = new_to_add
    return list_of_cuboids + to_add


# takes a list of non-overlapping cuboids and removes a cuboid
# result is again a list of non-overlapping cuboids
def combine_remove(list_of_cuboids, cuboid_to_remove):
    result = []
    for c in list_of_cuboids:
        result += minus(c, cuboid_to_remove)
    return result


print("start:", datetime.now())

on_cuboids = []  # list of non-overlapping cuboids
for line in lines:
    cmd, cuboid = parse_step(line)
    if included_in_part_1(cuboid):
        if cmd == "on":
            on_cuboids = combine_add(on_cuboids, cuboid)
        else:
            on_cuboids = combine_remove(on_cuboids, cuboid)
print("part 1:", sum([count(c) for c in on_cuboids]))

on_cuboids = []  # list of non-overlapping cuboids
for line in lines:
    cmd, cuboid = parse_step(line)
    if cmd == "on":
        on_cuboids = combine_add(on_cuboids, cuboid)
    else:
        on_cuboids = combine_remove(on_cuboids, cuboid)
print("part 2:", sum([count(c) for c in on_cuboids]))

print("finish:", datetime.now())

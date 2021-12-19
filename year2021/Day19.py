from collections import defaultdict

file = open("./year2021/data/day19.txt", "r")

# 48 rotation matrices including mirroring (hence 24x2)
R3D = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, -1]], [[1, 0, 0], [0, -1, 0], [0, 0, 1]],
       [[1, 0, 0], [0, -1, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
       [[1, 0, 0], [0, 0, -1], [0, 1, 0]], [[1, 0, 0], [0, 0, -1], [0, -1, 0]], [[-1, 0, 0], [0, 1, 0], [0, 0, 1]],
       [[-1, 0, 0], [0, 1, 0], [0, 0, -1]], [[-1, 0, 0], [0, -1, 0], [0, 0, 1]], [[-1, 0, 0], [0, -1, 0], [0, 0, -1]],
       [[-1, 0, 0], [0, 0, 1], [0, 1, 0]], [[-1, 0, 0], [0, 0, 1], [0, -1, 0]], [[-1, 0, 0], [0, 0, -1], [0, 1, 0]],
       [[-1, 0, 0], [0, 0, -1], [0, -1, 0]], [[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
       [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], [[0, 1, 0], [-1, 0, 0], [0, 0, -1]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
       [[0, 1, 0], [0, 0, 1], [-1, 0, 0]], [[0, 1, 0], [0, 0, -1], [1, 0, 0]], [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
       [[0, -1, 0], [1, 0, 0], [0, 0, 1]], [[0, -1, 0], [1, 0, 0], [0, 0, -1]], [[0, -1, 0], [-1, 0, 0], [0, 0, 1]],
       [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], [[0, -1, 0], [0, 0, 1], [1, 0, 0]], [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
       [[0, -1, 0], [0, 0, -1], [1, 0, 0]], [[0, -1, 0], [0, 0, -1], [-1, 0, 0]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
       [[0, 0, 1], [1, 0, 0], [0, -1, 0]], [[0, 0, 1], [-1, 0, 0], [0, 1, 0]], [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
       [[0, 0, 1], [0, 1, 0], [1, 0, 0]], [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
       [[0, 0, 1], [0, -1, 0], [-1, 0, 0]], [[0, 0, -1], [1, 0, 0], [0, 1, 0]], [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
       [[0, 0, -1], [-1, 0, 0], [0, 1, 0]], [[0, 0, -1], [-1, 0, 0], [0, -1, 0]], [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
       [[0, 0, -1], [0, 1, 0], [-1, 0, 0]], [[0, 0, -1], [0, -1, 0], [1, 0, 0]], [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]]


def read_inputs(file):
    inputs = []
    for line in [line.rstrip('\n') for line in file]:
        if "scanner" in line:
            beacon_coord = []
            inputs += [beacon_coord]
        elif line != "":
            beacon_coord += [list(map(int, line.split(",")))]
    return inputs


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def is_overlap(beacons, dist, a, b):
    match = [[], []]
    for i in range(len(beacons[a])):
        da = dist[(a, i)]
        for j in range(len(beacons[b])):
            db = dist[(b, j)]
            if len(da.intersection(db)) > 8:
                match[0] += [beacons[a][i]]
                match[1] += [beacons[b][j]]
                break
    if len(match[0]) >= 12:
        return match, True
    return [], False


def rotate_and_offset(rotation, offset, v):
    return [rotation[0][0] * v[0] + rotation[0][1] * v[1] + rotation[0][2] * v[2] + offset[0],
            rotation[1][0] * v[0] + rotation[1][1] * v[1] + rotation[1][2] * v[2] + offset[1],
            rotation[2][0] * v[0] + rotation[2][1] * v[1] + rotation[2][2] * v[2] + offset[2]]


def rotate_and_offset_all(rotation, offset, lv):
    return [rotate_and_offset(rotation, offset, v) for v in lv]


def calc_offset(lv1, lv2):
    offset = [lv2[0][0] - lv1[0][0], lv2[0][1] - lv1[0][1], lv2[0][2] - lv1[0][2]]
    for i in range(1, len(lv1)):
        for d in range(3):
            if lv2[i][d] - lv1[i][d] != offset[d]:
                return None
    return offset


def calc_rotation_and_offset(matching_beacons):
    x = matching_beacons[0]
    y = matching_beacons[1]
    for rotation in R3D:
        yr = rotate_and_offset_all(rotation, [0, 0, 0], y)
        offset = calc_offset(yr, x)
        if offset is not None:
            return rotation, offset
    return None, None


def add(rotat1, rotat2, offs1, offs2):
    rotation = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    offset = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            rotation[i][j] = rotat2[i][0] * rotat1[0][j] + rotat2[i][1] * rotat1[1][j] + rotat2[i][2] * rotat1[2][j]
        offset[i] = rotat2[i][0] * offs1[0] + rotat2[i][1] * offs1[1] + rotat2[i][2] * offs1[2] + offs2[i]
    return rotation, offset


beacons = read_inputs(file)
N = len(beacons)
ROT = [None] * N  # rotation of scanner i vs scanner 0 (rotation)
LIN = [None] * N  # offset of scanner i vs scanner 0 (linear component)
known = [False] * N  # do we know how to tranform the coordinates from scanner i into scanner 0 based coordinates
coord = defaultdict(list)  # coordinates of scanner i / beacon j (i,j) expressed in the coordinate system of scanner 0

ROT[0] = R3D[0]  # identity
LIN[0] = [0, 0, 0]  # zero offset
known[0] = True
for i in range(len(beacons[0])):
    coord[(0, i)] = beacons[0][i]

dist = defaultdict(set)  # manhattan distances of scanner i / beacon j (i,j) from othe beacons for same scanner
for s in range(N):
    for i in range(len(beacons[s])):
        for j in range(len(beacons[s])):
            if i != j:
                dist[(s, i)].add(manhattan_distance(beacons[s][i], beacons[s][j]))

stop = False
while not stop:
    stop = True
    for i in range(N):
        if known[i]:
            for j in range(N):
                if not known[j]:
                    matching_beacons, is_match = is_overlap(beacons, dist, i, j)
                    if is_match:
                        # print("match between scanners ", i, j)
                        rotation, offset = calc_rotation_and_offset(matching_beacons)
                        rotation0, offset0 = add(rotation, ROT[i], offset, LIN[i])  # rotation/offset vs scanner 0
                        ROT[j] = rotation0
                        LIN[j] = offset0
                        known[j] = True
                        stop = False

beacon_set = set()
for s in range(N):
    for i in range(len(beacons[s])):
        beacon_set.add(tuple(rotate_and_offset(ROT[s], LIN[s], beacons[s][i])))

print("Total number of beacons: ", len(beacon_set))

max_dist = 0
for s1 in range(N - 1):
    for s2 in range(s1 + 1, N):
        max_dist = max(max_dist, manhattan_distance(LIN[s1], LIN[s2]))
print("Max Manhattan distance between scanners: ", max_dist)

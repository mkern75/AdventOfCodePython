from typing import Optional
from math import isclose

INPUT_FILE = "./year2023/data/day24.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

PX, PY, PZ, VX, VY, VZ = 0, 1, 2, 3, 4, 5

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]
H = len(hailstones)


# part 1

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def calc_xy_intersection(hailstone1, hailstone2):
    x1, y1 = hailstone1[PX], hailstone1[PY]
    x2, y2 = hailstone1[PX] + hailstone1[VX], hailstone1[PY] + hailstone1[VY]
    x3, y3 = hailstone2[PX], hailstone2[PY]
    x4, y4 = hailstone2[PX] + hailstone2[VX], hailstone2[PY] + hailstone2[VY]
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    py = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    return None if d == 0 else (px / d, py / d)


ans1 = 0
test_area_min, test_area_max = 200000000000000, 400000000000000
for i in range(H - 1):
    for j in range(i + 1, H):
        res = calc_xy_intersection(hailstones[i], hailstones[j])
        if res is not None:
            time_i = (res[0] - hailstones[i][PX]) / hailstones[i][VX]
            time_j = (res[0] - hailstones[j][PX]) / hailstones[j][VX]
            if test_area_min <= min(res) <= max(res) <= test_area_max and 0 <= time_i and 0 <= time_j:
                ans1 += 1
print(f"part 1: {ans1}")


# part 2

# solves Ax = b
def gauss_elimination(a: list[list[float]], b: list[float]) -> Optional[list[float]]:
    N = len(b)
    assert len(a) == N
    assert all(len(row) == N for row in a)

    # solution vector
    x = [0.0] * N

    for i in range(N):
        # find pivot element (row)
        pivot = i
        for j in range(i + 1, N):
            if abs(a[j][i]) > abs(a[pivot][i]):
                pivot = j
        # check if value in pivot row is zero
        if a[pivot][i] == 0:
            return None
        # swap current and pivot row
        if pivot != i:
            a[i], a[pivot], b[i], b[pivot] = a[pivot], a[i], b[pivot], b[i]
        # ensure element in main diagonal is 1
        factor = 1.0 / a[i][i]
        for j in range(i, N):
            a[i][j] *= factor
        b[i] *= factor
        # forward elimination
        for j in range(i + 1, N):
            factor = - a[j][i] / a[i][i]
            for k in range(i + 1, N):
                a[j][k] += factor * a[i][k]
            b[j] += factor * b[i]
            a[j][i] = 0
    # backward substituion
    for i in range(N - 1, -1, -1):
        for j in range(i):
            factor = -a[j][i]
            a[j][i] += factor * a[i][i]
            b[j] += factor * b[i]
        x[i] = b[i]
    return x


# If we fix vx, vy of the rock, then we can work out the rock's position and velocity
# so that it collides with two given hailstones.
def solve_partial(hailstone1, hailstone2, vx_fixed, vy_fixed):
    x1, y1, z1, vx1, vy1, vz1 = hailstone1
    x2, y2, z2, vx2, vy2, vz2 = hailstone2
    a = [[0] * 4 for _ in range(4)]
    b = [0] * 4
    a[0][0] = 1
    a[0][2] = vx_fixed - vx1
    b[0] = x1
    a[1][0] = 1
    a[1][3] = vx_fixed - vx2
    b[1] = x2
    a[2][1] = 1
    a[2][2] = vy_fixed - vy1
    b[2] = y1
    a[3][1] = 1
    a[3][3] = vy_fixed - vy2
    b[3] = y2

    x = gauss_elimination(a, b)
    if x is None:
        return None
    x, y, t1, t2 = x

    vz = (z1 + t1 * vz1 - z2 - t2 * vz2) / (t1 - t2)
    z = z1 + t1 * vz1 - vz * t1

    return x, y, z, vx_fixed, vy_fixed, vz


# Given a candidate rock, check that it indeed collides with all hailstones.
def check_all(hailstones, rock):
    x, y, z, vx, vy, vz = rock
    for hailstone in hailstones:
        x1, y1, z1, vx1, vy1, vz1 = hailstone
        if (x - x1) * (vy1 - vy) != (y - y1) * (vx1 - vx):
            return False
        if (x - x1) * (vz1 - vz) != (z - z1) * (vx1 - vx):
            return False
        if (y - y1) * (vz1 - vz) != (z - z1) * (vy1 - vy):
            return False
    return True


v_min, v_max = -500, 500  # this is a simplifying assumption but it works
for vx_fixed in range(v_min, v_max + 1):
    for vy_fixed in range(v_min, v_max + 1):
        rock = solve_partial(hailstones[0], hailstones[1], vx_fixed, vy_fixed)
        if rock is not None:
            if all(isclose(f, round(f)) for f in rock):  # further assumption: integer solution
                rock = tuple(round(f) for f in rock)
                if check_all(hailstones, rock):
                    ans2 = round(rock[0]) + round(rock[1]) + round(rock[2])
                    print(f"part 2: {ans2}")
                    exit()

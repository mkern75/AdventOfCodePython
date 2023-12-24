from sympy import Symbol, solve

INPUT_FILE = "./year2023/data/day24.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

PX, PY, PZ, VX, VY, VZ = 0, 1, 2, 3, 4, 5

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]
H = len(hailstones)

# part 1
ans1 = 0
test_area_min, test_area_max = 200000000000000, 400000000000000
for i in range(H - 1):
    for j in range(i + 1, H):
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        x1, y1 = hailstones[i][PX], hailstones[i][PY]
        x2, y2 = hailstones[i][PX] + hailstones[i][VX], hailstones[i][PY] + hailstones[i][VY]
        x3, y3 = hailstones[j][PX], hailstones[j][PY]
        x4, y4 = hailstones[j][PX] + hailstones[j][VX], hailstones[j][PY] + hailstones[j][VY]
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        py = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        if d != 0:
            x = px / d
            y = py / d
            time_i = (x - hailstones[i][PX]) / hailstones[i][VX]
            time_j = (x - hailstones[j][PX]) / hailstones[j][VX]
            if test_area_min <= min(x, y) <= max(x, y) <= test_area_max and 0 <= time_i and 0 <= time_j:
                ans1 += 1
print(f"part 1: {ans1}")

# part 2
x1, y1, z1, vx1, vy1, vz1 = hailstones[0]
x2, y2, z2, vx2, vy2, vz2 = hailstones[1]
x3, y3, z3, vx3, vy3, vz3 = hailstones[2]

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
vx = Symbol("vx")
vy = Symbol("vy")
vz = Symbol("vz")
t1 = Symbol("t1")
t2 = Symbol("t2")
t3 = Symbol("t3")

equations = [x + t1 * vx - x1 - t1 * vx1,
             y + t1 * vy - y1 - t1 * vy1,
             z + t1 * vz - z1 - t1 * vz1,
             x + t2 * vx - x2 - t2 * vx2,
             y + t2 * vy - y2 - t2 * vy2,
             z + t2 * vz - z2 - t2 * vz2,
             x + t3 * vx - x3 - t3 * vx3,
             y + t3 * vy - y3 - t3 * vy3,
             z + t3 * vz - z3 - t3 * vz3]

res = solve(equations, [x, y, z, vx, vy, vz, t1, t2, t3], dict=True)
sol = res[0]
ans2 = sol[x] + sol[y] + sol[z]
print(f"part 2: {ans2}")

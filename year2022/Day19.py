import re
from collections import deque

INPUT_FILE = "./year2022/data/day19.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
blueprints = [tuple(map(int, re.findall(r"(-?\d+)", line))) for line in data]


def max_geodes(blueprint, time):
    # material required for building ore / clay / obsidian / geode robot
    material_required = [(blueprint[1], 0, 0, 0),
                         (blueprint[2], 0, 0, 0),
                         (blueprint[3], blueprint[4], 0, 0),
                         (blueprint[5], 0, blueprint[6], 0)]

    queue = deque([(time, (0, 0, 0, 0), (1, 0, 0, 0), -1)])
    geo_max = 0

    while queue:

        t, m, r, n = queue.popleft()  # time, material (tuple), robots (tuple), what robot to build next

        if t == 0:
            geo_max = max(geo_max, m[3])
            continue

        geo_max_upper_bound = m[3] + t * r[3] + t * (t - 1) // 2
        if geo_max_upper_bound <= geo_max:
            continue

        if n == -1:
            for n in range(4):
                if all(m[i] >= material_required[n][i] or r[i] > 0 for i in range(4)):
                    queue.appendleft((t, m, r, n))
            continue

        if all(m[i] >= material_required[n][i] for i in range(4)):
            queue.appendleft((t - 1,
                              tuple(m[i] - material_required[n][i] + r[i] for i in range(4)),
                              tuple(r[i] + 1 if i == n else r[i] for i in range(4)),
                              -1))
            continue

        queue.appendleft((t - 1, tuple(m[i] + r[i] for i in range(4)), r, n))

    return geo_max


ans1, T = 0, 24
for i in range(len(blueprints)):
    print(f"starting blueprint {blueprints[i][0]} for {T} minutes: ", end="")
    n_geodes = max_geodes(blueprints[i], T)
    print(f"{n_geodes} geode collected")
    ans1 += n_geodes * blueprints[i][0]
print(f"part 1: {ans1}")  # PyPy: 26s

ans2, T = 1, 32
for i in range(3):
    print(f"starting blueprint {blueprints[i][0]} for {T} minutes: ", end="")
    n_geodes = max_geodes(blueprints[i], T)
    print(f"{n_geodes} geode collected")
    ans2 *= n_geodes
print(f"part 2: {ans2}")  # PyPy: 236s

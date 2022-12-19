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

    # additional idea from other AoC users - upper bounds for number of robots required:
    # e.g. if any robot requires at most k ore, then we never need more than k ore robots
    robots_max_required = [max(material_required[j][i] for j in range(4)) for i in range(3)] + [time]

    queue, visited = deque([(time, (0, 0, 0, 0), (1, 0, 0, 0), -1)]), set()
    geo_max = 0

    while queue:

        t, m, r, n = queue.popleft()  # time, material (tuple), robots (tuple), what robot to build next

        if (t, m, r, n) in visited:
            continue
        visited.add((t, m, r, n))

        if t == 0:
            geo_max = max(geo_max, m[3])
            continue

        geo_max_upper_bound = m[3] + t * r[3] + t * (t - 1) // 2
        if geo_max_upper_bound <= geo_max:
            continue

        if n == -1:
            for n in range(4):
                if r[n] < robots_max_required[n]:
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


# overall less than 5s with PyPy
ans1, T = 0, 24
for i in range(len(blueprints)):
    print(f"starting blueprint {blueprints[i][0]} for {T} minutes: ", end="")
    n_geodes = max_geodes(blueprints[i], T)
    print(f"{n_geodes} geode collected")
    ans1 += n_geodes * blueprints[i][0]
print(f"part 1: {ans1}")

ans2, T = 1, 32
for i in range(3):
    print(f"starting blueprint {blueprints[i][0]} for {T} minutes: ", end="")
    n_geodes = max_geodes(blueprints[i], T)
    print(f"{n_geodes} geode collected")
    ans2 *= n_geodes
print(f"part 2: {ans2}")

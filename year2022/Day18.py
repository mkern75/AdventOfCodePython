INPUT_FILE = "./year2022/data/day18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
cubes = set(tuple(map(int, line.split(","))) for line in data)

cache = {}  # caching results for whether cube is trapped
coord_min = [min(cube[i] for cube in cubes) for i in range(3)]
coord_max = [max(cube[i] for cube in cubes) for i in range(3)]


def neighbours(cube):
    """ Returns the six neighbour cubes."""
    return [(cube[0] + d0, cube[1] + d1, cube[2] + d2) for d0, d1, d2 in
            [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]]


def is_trapped(cube):
    if cube in cache:
        return cache[cube]
    queue, visited = [cube], {cube}
    while queue:
        c = queue.pop()
        if any(c[i] <= coord_min[i] or c[i] >= coord_max[i] for i in range(3)):  # at border => not trapped
            cache[c] = False
        if c in cache:  # already known => save results for all visited cubes
            for cv in visited:
                cache[cv] = cache[c]
            return cache[cube]
        for cn in neighbours(c):  # explore 6 neighbours
            if cn not in visited and cn not in cubes:
                queue.append(cn)
                visited.add(cn)
    for c in visited:  # if none of the explored connected cubes is on the outside, then all these cubes are trapped
        cache[c] = True
    return cache[cube]


ans1, ans2 = 0, 0
for cube in cubes:
    for neighbour in neighbours(cube):
        if neighbour not in cubes:
            ans1 += 1
            ans2 += int(not is_trapped(neighbour))
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

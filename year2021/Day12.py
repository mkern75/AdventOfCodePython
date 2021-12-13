from collections import defaultdict

file = open("./year2021/data/day12.txt", "r")
lines = [line.rstrip('\n') for line in file]


def count_paths(path, conn, allow_twice=False):
    if path[-1] == "end":
        return 1
    cnt = 0
    for neighbour in conn[path[-1]]:
        if neighbour.isupper() or neighbour not in path:
            cnt += count_paths(path + [neighbour], conn, allow_twice)
        elif allow_twice and neighbour not in ["start", "end"]:
            cnt += count_paths(path + [neighbour], conn, False)
    return cnt


conn = defaultdict(list)
for line in lines:
    cave1, cave2 = line.split("-")
    conn[cave1].append(cave2)
    conn[cave2].append(cave1)
print(count_paths(["start"], conn))
print(count_paths(["start"], conn, True))

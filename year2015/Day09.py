from collections import defaultdict

file = open("./year2015/data/day09.txt", "r")
lines = [line.rstrip('\n') for line in file]

L = set([])  # locations
D = defaultdict(int)  # distances between locations

for line in lines:
    s = line.split()
    loc1, loc2, dist = s[0], s[2], int(s[4])
    L.update(set([loc1, loc2]))
    D[(loc1, loc2)] = dist
    D[(loc2, loc1)] = dist


def visit(dist, path, unvisited, is_min):
    if len(unvisited) == 0:
        return dist
    best_dist = 1e10 if is_min else -1
    for loc in unvisited:
        new_dist = dist + (D[(path[-1], loc)] if len(path) > 0 else 0)
        total_dist = visit(new_dist, path + [loc], unvisited - set([loc]), is_min)
        if (is_min and total_dist < best_dist) or (not is_min and total_dist > best_dist):
            best_dist = total_dist
    return best_dist


print(visit(0, [], L, True))
print(visit(0, [], L, False))

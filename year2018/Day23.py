from utils import load_lines, tic, toc, manhatten_dist
import heapq
import re
from collections import namedtuple

# this solution works well for the AoC input but does not necessarily work well (fast) for any input

INPUT_FILE = "./year2018/data/day23.txt"
Nanobot = namedtuple("nanobot", "pos r")


def load_nanobots(filename):
    nanobots = []
    for line in load_lines(filename):
        x, y, z, r = map(int, re.findall(r"(-?\d+)", line))
        nanobots += [Nanobot([x, y, z], r)]
    return nanobots


# whether a nanobot overlaps with a box
def is_overlap(nanobot, x_min, x_max, y_min, y_max, z_min, z_max):
    x, y, z, r = nanobot.pos[0], nanobot.pos[1], nanobot.pos[2], nanobot.r
    dx = 0 if x_min <= x <= x_max else min(abs(x - x_min), abs(x - x_max))
    dy = 0 if y_min <= y <= y_max else min(abs(y - y_min), abs(y - y_max))
    dz = 0 if z_min <= z <= z_max else min(abs(z - z_min), abs(z - z_max))
    return dx + dy + dz <= r


# counts the number of nanobots that overlap with a box
def count_overlaps(nanobots, x_min, x_max, y_min, y_max, z_min, z_max):
    n_overlaps = 0
    for nanobot in nanobots:
        if is_overlap(nanobot, x_min, x_max, y_min, y_max, z_min, z_max):
            n_overlaps += 1
    return n_overlaps


# shortest manhattan distance from a box to the origin (0,0,0)
def dist_box_to_orig(x_min, x_max, y_min, y_max, z_min, z_max):
    dx = 0 if x_min <= 0 <= x_max else min(abs(x_min), abs(x_max))
    dy = 0 if y_min <= 0 <= y_max else min(abs(y_min), abs(y_max))
    dz = 0 if z_min <= 0 <= z_max else min(abs(z_min), abs(z_max))
    return dx + dy + dz


def search(nanobots):
    n_overlap_best, dist_best = -1, 0

    x_min = min([nanobot.pos[0] - nanobot.r for nanobot in nanobots])
    x_max = max([nanobot.pos[0] + nanobot.r for nanobot in nanobots])
    y_min = min([nanobot.pos[1] - nanobot.r for nanobot in nanobots])
    y_max = max([nanobot.pos[1] + nanobot.r for nanobot in nanobots])
    z_min = min([nanobot.pos[2] - nanobot.r for nanobot in nanobots])
    z_max = max([nanobot.pos[2] + nanobot.r for nanobot in nanobots])
    n_overlap = len(nanobots)
    dist_from_orig = dist_box_to_orig(x_min, x_max, y_min, y_max, z_min, z_max)

    # search through smaller and smaller 3D boxes and prioritise

    # first criteria: number of overlaps of nanobots with box
    # second criteria: shortest distance from box to origin
    # minus sign as heapq is min-heap
    priority = - (n_overlap + 1.0 / (2.0 + dist_from_orig))

    q = []
    heapq.heappush(q, (priority, (n_overlap, dist_from_orig, x_min, x_max, y_min, y_max, z_min, z_max)))

    while len(q) > 0:

        priority, (n_overlap, dist_from_origin, x1, x2, y1, y2, z1, z2) = heapq.heappop(q)

        # if best solution from queue is worse than best found solution so far: return best results found
        if n_overlap < n_overlap_best or n_overlap == n_overlap_best and dist_from_origin > dist_best:
            return n_overlap_best, dist_best

        # box with exactly one coordinate: check whether it's an improvement
        if x1 == x2 and y1 == y2 and z1 == z2:
            dist = manhatten_dist((x1, y1, z1), (0, 0, 0))
            if n_overlap > n_overlap_best:
                n_overlap_best, dist_best = n_overlap, dist
            elif n_overlap == n_overlap_best and dist < dist_best:
                dist_best = dist

        # otherwise, divide box into smaller boxes and add them to heap
        else:
            x_set, y_set, z_set = set(), set(), set()
            xm, ym, zm = (x1 + x2) // 2, (y1 + y2) // 2, (z1 + z2) // 2
            x_set.add((x1, xm))
            if xm + 1 <= x2:
                x_set.add((xm + 1, x2))
            y_set.add((y1, ym))
            if ym + 1 <= y2:
                y_set.add((ym + 1, y2))
            z_set.add((z1, zm))
            if zm + 1 <= z2:
                z_set.add((zm + 1, z2))

            for (xf, xt) in x_set:
                for (yf, yt) in y_set:
                    for (zf, zt) in z_set:
                        n_overlap_new = count_overlaps(nanobots, xf, xt, yf, yt, zf, zt)
                        dist_from_origin_new = dist_box_to_orig(xf, xt, yf, yt, zf, zt)
                        priority = - (n_overlap_new + 1.0 / (2.0 + dist_from_origin_new))
                        heapq.heappush(q, (priority, (n_overlap_new, dist_from_origin_new, xf, xt, yf, yt, zf, zt)))

    return n_overlap_best, dist_best


tic()
nanobots = load_nanobots(INPUT_FILE)

nanobot_best = nanobots[0]
for nanobot in nanobots:
    if nanobot.r > nanobot_best.r:
        nanobot_best = nanobot
ans1 = sum([1 for nanobot in nanobots if manhatten_dist(nanobot.pos, nanobot_best.pos) <= nanobot_best.r])
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
_, ans2 = search(nanobots)
print(f"part 2: {ans2}   ({toc():.3f}s)")

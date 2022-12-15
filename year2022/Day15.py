import re

INPUT_FILE = "./year2022/data/day15.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
sensors = [tuple(map(int, re.findall(r"(-?\d+)", line))) for line in data]


def merge(r_from, r_to, range_list):
    """Merges a range [r_from, r_to] into a list of non-overlallping ranges."""
    range_list_tmp = []
    for i, (r2_from, r2_to) in enumerate(range_list):
        if r2_from <= r_from <= r_to <= r2_to:
            return range_list
        elif r_from <= r2_from <= r2_to <= r_to:
            continue
        elif r_to < r2_from:
            return range_list_tmp + [(r_from, r_to)] + range_list[i:]
        elif r2_to < r_from:
            range_list_tmp += [(r2_from, r2_to)]
        else:
            r_from = min(r_from, r2_from)
            r_to = max(r_to, r2_to)
    return range_list_tmp + [(r_from, r_to)]


def calc_x_ranges_with_no_beacons(y):
    """Calculates the ranges of x coordinates for a given y coordinate that are without beacons."""
    no_beacons = []
    for xs, ys, xb, yb in sensors:
        d = abs(xs - xb) + abs(ys - yb)
        dy = abs(ys - y)
        if dy <= d:
            dx = d - dy
            x1 = xs - dx
            x2 = xs + dx
            if (x1, y) == (xb, yb):
                x1 += 1
            if (x2, y) == (xb, yb):
                x2 -= 1
            if x1 <= x2:
                no_beacons = merge(x1, x2, no_beacons)
    return no_beacons


def count_positions(ranges, consider_from=None, consider_to=None):
    """Counts the number of positions covered by a list of ranges. Lower and upper thresholds can be provided."""
    total = 0
    for value_from, value_to in ranges:
        if consider_from is not None:
            if value_to < consider_from:
                continue
            value_from = max(value_from, consider_from)
        if consider_to is not None:
            if consider_to < value_from:
                continue
            value_to = min(value_to, consider_to)
        total += value_to - value_from + 1
    return total


# part 1
ranges_with_no_beacon = calc_x_ranges_with_no_beacons(2_000_000)
ans1 = count_positions(ranges_with_no_beacon)
print(f"part 1: {ans1}")

#  part 2 (Python: 32s, PyPy: 16s)
pos_min, pos_max = 0, 4_000_000
for y in range(pos_min, pos_max + 1):
    ranges_with_no_beacon = calc_x_ranges_with_no_beacons(y)
    n_no_beacons = count_positions(ranges_with_no_beacon, pos_min, pos_max)
    known_beacons = set((xb, yb) for _, _, xb, yb in sensors if yb == y and pos_min <= xb <= pos_max)
    n_known_beacons = len(known_beacons)
    n_unknown_beacons = pos_max - pos_min + 1 - n_no_beacons - n_known_beacons
    if n_unknown_beacons != 0:
        x_candidates = set([v_from - 1 for v_from, _ in ranges_with_no_beacon if pos_min <= v_from - 1 <= pos_max])
        x_candidates |= set([v_to + 1 for _, v_to in ranges_with_no_beacon if pos_min <= v_to + 1 <= pos_max])
        x_candidates -= set(xb for xb, _ in known_beacons)
        x, = x_candidates
        ans2 = x * 4_000_000 + y
        print(f"part 2: {ans2}")
        break

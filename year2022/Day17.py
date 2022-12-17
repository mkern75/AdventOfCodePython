from collections import defaultdict

ROCKS = [[list("####")],
         [list(".#."), list("###"), list(".#.")],
         [list("..#"), list("..#"), list("###")],
         [list("#"), list("#"), list("#"), list("#")],
         [list("##"), list("##")]]

INPUT_FILE = "./year2022/data/day17.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")][0]


def can_move(rock, r, c, dr, dc):
    nr, nc = len(rock), len(rock[0])
    if c + dc < 0 or c + nc + dc >= 8:
        return False
    for rr in range(nr):
        for cc in range(nc):
            if rock[rr][cc] == chamber[r - rr + dr, c + cc + dc] == "#":
                return False
    return True


def rest(rock, r, c):
    nr, nc = len(rock), len(rock[0])
    for rr in range(nr):
        for cc in range(nc):
            if rock[rr][cc] == "#":
                chamber[r - rr, c + cc] = "#"


def bitmask_for_columns(r_max, n_rows):
    res = []
    for c in range(7):
        bitmask, bit = 0, 1
        for r in range(r_max, r_max - n_rows, -1):
            if chamber[r, c] == "#":
                bitmask |= bit
            bit <<= 1
        res += [bitmask]
    return tuple(res)


def simulate_single_rock(rock, jet_idx, top):
    r, c = top + 3 + len(rock), 2
    while True:
        if data[jet_idx] == "<" and can_move(rock, r, c, 0, -1):
            c -= 1
        elif data[jet_idx] == ">" and can_move(rock, r, c, 0, 1):
            c += 1
        jet_idx = (jet_idx + 1) % len(data)
        if can_move(rock, r, c, -1, 0):
            r -= 1
        else:
            rest(rock, r, c)
            top = max(top, r)
            return jet_idx, top


def simulate(n_rocks):
    idx, top = 0, -1
    for cycle in range(n_rocks):
        idx, top = simulate_single_rock(ROCKS[cycle % len(ROCKS)], idx, top)
    return top + 1


def simulate2(n_rocks):
    jet_idx, top, cycle = 0, -1, 0
    hist, seen = {}, {}
    while True:
        rock_index = cycle % len(ROCKS)
        jet_idx, top = simulate_single_rock(ROCKS[rock_index], jet_idx, top)
        signature = (rock_index, jet_idx) + bitmask_for_columns(top, 64)
        hist[cycle] = top
        if signature in seen:
            break
        seen[signature] = cycle
        cycle += 1
    curr, prev = cycle, seen[signature]
    delta_cycle = curr - prev
    delta_top = hist[curr] - hist[prev]
    q, r = divmod(n_rocks - 1 - prev, delta_cycle)
    top = hist[prev] + q * delta_top + (hist[prev + r] - hist[prev])
    return top + 1


chamber = defaultdict(lambda: ".", {(-1, c): "#" for c in range(7)})
print(f"part 1: {simulate(2022)}")

chamber = defaultdict(lambda: ".", {(-1, c): "#" for c in range(7)})
print(f"part 2: {simulate2(1000000000000)}")

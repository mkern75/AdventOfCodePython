ROCKS = [[list("####")],
         [list(".#."), list("###"), list(".#.")],
         [list("..#"), list("..#"), list("###")],
         [list("#"), list("#"), list("#"), list("#")],
         [list("##"), list("##")]]

INPUT_FILE = "./year2022/data/day17.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")][0]


def get_rock(rock_idx, r, c):
    nr, nc = len(ROCKS[rock_idx]), len(ROCKS[rock_idx][0])
    return set((r + nr - 1 - rr, c + cc) for rr in range(nr) for cc in range(nc) if ROCKS[rock_idx][rr][cc] == "#")


def move(rock, dr, dc):
    return set((r + dr, c + dc) for r, c, in rock)


def can_move(chamber, rock, dr, dc):
    p = move(rock, dr, dc)
    return not (any(c < 0 or c > 6 for r, c in p) or p & chamber)


def simulate_single_rock(chamber, rock_idx, jet_idx, top):
    rock = get_rock(rock_idx, top + 4, 2)
    while True:
        if data[jet_idx] == "<" and can_move(chamber, rock, 0, -1):
            rock = move(rock, 0, -1)
        elif data[jet_idx] == ">" and can_move(chamber, rock, 0, 1):
            rock = move(rock, 0, 1)
        jet_idx = (jet_idx + 1) % len(data)
        if can_move(chamber, rock, -1, 0):
            rock = move(rock, -1, 0)
        else:
            chamber |= rock
            top = max(top, max(r for r, c in rock))
            return jet_idx, top


def simulate(n_rocks):
    chamber = {(0, c) for c in range(7)}  # border at row zero
    jet_idx, top, cycle = 0, 0, 0
    hist, seen = {}, {}
    while True:
        rock_index = cycle % len(ROCKS)
        jet_idx, top = simulate_single_rock(chamber, rock_index, jet_idx, top)
        signature = (rock_index, jet_idx) + tuple(
            (1 if (r, c) in chamber else 0) for c in range(7) for r in range(top - 63, top + 1))
        hist[cycle] = top
        if signature in seen:
            break
        seen[signature] = cycle
        cycle += 1
        if cycle == n_rocks:
            return top
    curr, prev = cycle, seen[signature]
    delta_cycle = curr - prev
    delta_top = hist[curr] - hist[prev]
    q, r = divmod(n_rocks - 1 - prev, delta_cycle)
    top = hist[prev] + q * delta_top + (hist[prev + r] - hist[prev])
    return top


print(f"part 1: {simulate(2022)}")
print(f"part 2: {simulate(1000000000000)}")

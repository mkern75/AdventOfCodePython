ROCKS = [[list("####")],
         [list(".#."), list("###"), list(".#.")],
         [list("..#"), list("..#"), list("###")],
         [list("#"), list("#"), list("#"), list("#")],
         [list("##"), list("##")]]

INPUT_FILE = "./year2022/data/day17.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")][0]


def get_rock(rock_idx, x, y):
    nx, ny = len(ROCKS[rock_idx][0]), len(ROCKS[rock_idx])
    return set((x + xx, y + ny - 1 - yy) for xx in range(nx) for yy in range(ny) if ROCKS[rock_idx][yy][xx] == "#")


def move(rock, dx, dy):
    return set((x + dx, y + dy) for x, y, in rock)


def can_move(chamber, rock, dx, dy):
    p = move(rock, dx, dy)
    return not (any(x < 0 or x > 6 for x, y in p) or p & chamber)


def simulate_single_rock(chamber, rock_idx, jet_idx, top):
    rock = get_rock(rock_idx, 2, top + 4)
    while True:
        if data[jet_idx] == "<" and can_move(chamber, rock, -1, 0):
            rock = move(rock, -1, 0)
        elif data[jet_idx] == ">" and can_move(chamber, rock, 1, 0):
            rock = move(rock, 1, 0)
        jet_idx = (jet_idx + 1) % len(data)
        if can_move(chamber, rock, 0, -1):
            rock = move(rock, 0, -1)
        else:
            chamber |= rock
            top = max(top, max(y for x, y in rock))
            return jet_idx, top


def simulate(n_rocks):
    chamber = {(x, -1) for x in range(7)}
    jet_idx, top = 0, -1
    for cycle in range(n_rocks):
        jet_idx, top = simulate_single_rock(chamber, cycle % len(ROCKS), jet_idx, top)
    return top + 1


def simulate2(n_rocks):
    chamber = {(x, -1) for x in range(7)}
    jet_idx, top, cycle = 0, -1, 0
    hist, seen = {}, {}
    while True:
        rock_index = cycle % len(ROCKS)
        jet_idx, top = simulate_single_rock(chamber, rock_index, jet_idx, top)
        signature = (rock_index, jet_idx) + tuple(
            (1 if (x, y) in chamber else 0) for x in range(7) for y in range(top - 63, top + 1))
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


print(f"part 1: {simulate(2022)}")
print(f"part 2: {simulate2(1000000000000)}")

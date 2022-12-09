INPUT_FILE = "./year2020/data/day17.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def neighbours(cube):
    nb = []
    for xn in range(cube[0] - 1, cube[0] + 2):
        for yn in range(cube[1] - 1, cube[1] + 2):
            for zn in range(cube[2] - 1, cube[2] + 2):
                if len(cube) == 3:  # part 1
                    if (xn, yn, zn) != cube:
                        nb += [(xn, yn, zn)]
                elif len(cube) == 4:  # part 2
                    for wn in range(cube[3] - 1, cube[3] + 2):
                        if (xn, yn, zn, wn) != cube:
                            nb += [(xn, yn, zn, wn)]
    return nb


def get_n_active_neighbours(cube, active):
    return sum(c in active for c in neighbours(cube))


def run_one_cycle(active):
    active_new = set()
    to_check = set()
    for cube in active:
        to_check.update([cube] + neighbours(cube))
    for cube in to_check:
        n = get_n_active_neighbours(cube, active)
        if (cube in active and n in [2, 3]) or (cube not in active and n == 3):
            active_new.add(cube)
    return active_new


# part 1
active = set([(x, y, 0) for x, line in enumerate(data) for y, f in enumerate(line) if f == "#"])
for _ in range(6):
    active = run_one_cycle(active)
print(f"part 1: {len(active)}")

# part 2
active = set([(x, y, 0, 0) for x, line in enumerate(data) for y, f in enumerate(line) if f == "#"])
for _ in range(6):
    active = run_one_cycle(active)
print(f"part 2: {len(active)}")

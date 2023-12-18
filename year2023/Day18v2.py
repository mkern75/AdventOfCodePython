INPUT_FILE = "./year2023/data/day18.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

MOVE = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0),
        "2": (0, -1), "0": (0, 1), "3": (-1, 0), "1": (1, 0)}


def solve(instructions):
    v = [(0, 0)]
    for direction, distance in instructions[:-1]:
        r, c = v[-1]
        dr, dc = MOVE[direction]
        v += [(r + distance * dr, c + distance * dc)]
    n = len(v)

    # https://en.wikipedia.org/wiki/Shoelace_formula &  https://en.wikipedia.org/wiki/Pick%27s_theorem
    area = abs(sum((v[i][1] + v[(i + 1) % n][1]) * (v[i][0] - v[(i + 1) % n][0]) for i in range(n))) // 2
    boundary_points = sum(abs(v[i][0] - v[(i + 1) % n][0]) + abs(v[i][1] - v[(i + 1) % n][1]) for i in range(n))
    interior_points = area + 1 - boundary_points // 2
    return boundary_points + interior_points


# part 1
instructions = [(line.split()[0], int(line.split()[1])) for line in data]
ans1 = solve(instructions)
print(f"part 1: {ans1}")

# part 2
instructions = [(line.split()[2][7], int(line.split()[2][2:7], 16)) for line in data]
ans2 = solve(instructions)
print(f"part 2: {ans2}")

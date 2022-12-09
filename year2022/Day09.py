INPUT_FILE = "./year2022/data/day09.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

MOVE = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def sgn(n):
    return 1 if n > 0 else (-1 if n < 0 else 0)


def follow(head, tail):
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    return tail if abs(dx) <= 1 and abs(dy) <= 1 else (tail[0] + sgn(dx), tail[1] + sgn(dy))


def n_positions(n_knots):
    knots = [(0, 0) for _ in range(n_knots)]
    visited = {knots[-1]}
    for motion in data:
        direction, steps = motion.split()
        for _ in range(int(steps)):
            knots[0] = (knots[0][0] + MOVE[direction][0], knots[0][1] + MOVE[direction][1])
            for i in range(1, n_knots):
                knots[i] = follow(knots[i - 1], knots[i])
            visited |= {knots[-1]}
    return len(visited)


print(f"part 1: {n_positions(2)}")
print(f"part 2: {n_positions(10)}")

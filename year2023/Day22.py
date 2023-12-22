INPUT_FILE = "./year2023/data/day22.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

GROUND = -1
X, Y, Z = 0, 1, 2

bricks = []
for line in data:
    coord1, coord2 = line.split("~")
    bricks += [(list(map(int, coord1.split(","))), list(map(int, coord2.split(","))))]
N = len(bricks)


def is_overlap(brick1, brick2):
    return not (brick1[1][X] < brick2[0][X] or brick1[0][X] > brick2[1][X] or
                brick1[1][Y] < brick2[0][Y] or brick1[0][Y] > brick2[1][Y])


def top(brick):
    return max(brick[0][Z], brick[1][Z])


def bottom(brick):
    return min(brick[0][Z], brick[1][Z])


def move_down(brick, target_bottom_z):
    fall = bottom(brick) - target_bottom_z
    brick[0][Z] -= fall
    brick[1][Z] -= fall


# sort bricks by increasing bottom / Z value
bricks.sort(key=lambda brick: bottom(brick))

rests_on = [[] for _ in range(N)]
for i, brick in enumerate(bricks):
    overlaps_below = {j for j in range(i) if is_overlap(brick, bricks[j])}
    if overlaps_below:
        max_top = max(top(bricks[j]) for j in overlaps_below)
        rests_on[i] = [j for j in overlaps_below if top(bricks[j]) == max_top]
        move_down(brick, max_top + 1)
    else:
        rests_on[i] += [GROUND]
        move_down(brick, 1)

can_be_disintegrated = [True] * N
for i in range(N):
    if len(rests_on[i]) == 1 and rests_on[i][0] != GROUND:
        can_be_disintegrated[rests_on[i][0]] = False
ans1 = sum(can_be_disintegrated)
print(f"part 1: {ans1}")

ans2 = 0
for i in range(N):
    if not can_be_disintegrated[i]:
        gone = {i}
        for j in range(i + 1, N):
            if set(rests_on[j]).issubset(gone):
                gone |= {j}
        ans2 += len(gone) - 1
print(f"part 2: {ans2}")

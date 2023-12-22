INPUT_FILE = "./year2023/data/day22.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

GROUND = -1

bricks = []
for line in data:
    start, end = line.split("~")
    bricks += [(list(map(int, start.split(","))), list(map(int, end.split(","))))]
N = len(bricks)


def do_overlap(b1, b2):
    return not (b1[1][0] < b2[0][0] or b1[0][0] > b2[1][0] or b1[1][1] < b2[0][1] or b1[0][1] > b2[1][1])


def top(b):
    return max(b[0][2], b[1][2])


def bottom(b):
    return min(b[0][2], b[1][2])


bricks.sort(key=lambda b: bottom(b))
rests_on = [[] for _ in range(N)]

for i in range(N):
    overlaps_below = {j for j in range(i) if do_overlap(bricks[i], bricks[j])}
    if overlaps_below:
        top_max = max(top(bricks[k]) for k in overlaps_below)
        rests_on[i] += [k for k in overlaps_below if top(bricks[k]) == top_max]
        fall = bottom(bricks[i]) - (top_max + 1)
    else:
        rests_on[i] += [GROUND]
        fall = bottom(bricks[i]) - 1
    bricks[i][0][2] -= fall
    bricks[i][1][2] -= fall

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

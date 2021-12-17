file = open("./year2021/data/day17.txt", "r")
lines = [line.rstrip('\n') for line in file]


# returns highest y position reached if target area was hit, and None otherwise
def simulate(vx, vy, trgt_x1, trgt_x2, trgt_y1, trgt_y2):
    x, y, y_max = 0, 0, 0
    hit = False
    while True:
        x += vx
        y += vy
        vx = (vx - 1 if vx > 0 else (vx + 1 if vx < 0 else 0))
        vy -= 1
        y_max = max(y_max, y)
        hit = hit or (trgt_x1 <= x <= trgt_x2 and trgt_y1 <= y <= trgt_y2)
        if x > trgt_x2 or (vx == 0 and (x < trgt_x1 or y < trgt_y1)):
            return y_max if hit else None


s = lines[0].split(":")[1].split(", ")
trgt_x1, trgt_x2 = map(int, s[0].replace("x=", "").split(".."))
trgt_y1, trgt_y2 = map(int, s[1].replace("y=", "").split(".."))

y_max, cnt = 0, 0
for vx in range(1, trgt_x2 + 1):
    for vy in range(trgt_y1, trgt_x2 + 1):
        y_high = simulate(vx, vy, trgt_x1, trgt_x2, trgt_y1, trgt_y2)
        if y_high is not None:
            y_max = max(y_max, y_high)
            cnt += 1
print(y_max)
print(cnt)

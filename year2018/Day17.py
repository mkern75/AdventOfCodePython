from utils import load_lines
from collections import defaultdict, deque
import re

INPUT_FILE = "./year2018/data/day17.txt"

# dictionary to store the different fields
ground = defaultdict(lambda: ".")
ground[500, 0] = "|"  # spring

# load clay data
for line in load_lines(INPUT_FILE):
    p = re.compile(r"([xy])=(\d+), ([xy])=(\d+)..(\d+)").match(line)
    if p.group(1) == "x":
        for y in range(int(p.group(4)), int(p.group(5)) + 1):
            ground[int(p.group(2)), y] = "#"
    elif p.group(1) == "y":
        for x in range(int(p.group(4)), int(p.group(5)) + 1):
            ground[x, int(p.group(2))] = "#"
y_min, y_max = min([c[1] for c in ground if ground[c] == "#"]), max([c[1] for c in ground if ground[c] == "#"])

# queue to track water flow
q_flow = deque([(500, 0)])  # spring

while len(q_flow) > 0:

    # flow water
    while len(q_flow) > 0:
        x, y = q_flow.popleft()
        if ground[x, y + 1] == "." and y < y_max:
            ground[x, y + 1] = "|"
            q_flow.append((x, y + 1))
        elif ground[x, y + 1] in ["#", "~"]:
            if ground[x - 1, y] == ".":
                ground[x - 1, y] = "|"
                q_flow.append((x - 1, y))
            if ground[x + 1, y] == ".":
                ground[x + 1, y] = "|"
                q_flow.append((x + 1, y))

    # settle water
    flowing_water = [pos for pos, g in ground.items() if g == "|"]
    for (x, y) in flowing_water:
        if ground[x - 1, y] in ["#", "~"] and ground[x, y + 1] in ["#", "~"]:
            x_start = x_end = x
            while ground[x_end + 1, y] == "|" and ground[x_end + 1, y + 1] in ["#", "~"]:
                x_end += 1
            if ground[x_end + 1, y] == "#":
                for x_settle in range(x_start, x_end + 1):
                    ground[x_settle, y] = "~"
                    if ground[x_settle, y - 1] == "|":
                        q_flow.append((x_settle, y - 1))

ans1 = len([g for pos, g in ground.items() if g in ["|", "~"] and y_min <= pos[1] <= y_max])
print("part 1:", ans1)

ans2 = len([g for g in ground.values() if g == "~"])
print("part 2:", ans2)

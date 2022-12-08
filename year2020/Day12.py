INPUT_FILE = "./year2020/data/day12.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

MOVE = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}

x, y, dx, dy = 0, 0, 1, 0
for instruction in data:
    action, val = instruction[0], int(instruction[1:])
    if action in ["N", "S", "W", "E"]:
        x, y = x + val * MOVE[action][0], y + val * MOVE[action][1]
    elif action == "F":
        x, y = x + val * dx, y + val * dy
    else:
        for _ in range(val // 90 if action == "L" else (360 - val) // 90):
            dx, dy = -dy, dx
print(f"part 1: {abs(x) + abs(y)}")

x, y, wx, wy = 0, 0, 10, 1
for instruction in data:
    action, val = instruction[0], int(instruction[1:])
    if action in ["N", "S", "W", "E"]:
        wx, wy = wx + val * MOVE[action][0], wy + val * MOVE[action][1]
    elif action == "F":
        x, y = x + val * wx, y + val * wy
    else:
        for _ in range(val // 90 if action == "L" else (360 - val) // 90):
            wx, wy = -wy, wx
print(f"part 2: {abs(x) + abs(y)}")

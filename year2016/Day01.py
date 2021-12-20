from collections import Counter

file = open("./year2016/data/day01.txt", "r")
lines = [line.rstrip('\n') for line in file]

x, y = 0, 0
dx, dy = 0, 1
visited = Counter([(0, 0)])
ans2 = -1

for move in [x.strip() for x in lines[0].split(",")]:
    if move[0] == "L":
        dx, dy = -dy, dx
    elif move[0] == "R":
        dx, dy = dy, -dx
    for i in range(1, int(move[1:]) + 1):
        x, y = x + dx, y + dy
        visited[(x, y)] += 1
        if ans2 == -1 and visited[(x, y)] > 1:
            ans2 = abs(x) + abs(y)
ans1 = abs(x) + abs(y)
print("part 1:", ans1)
print("part 2:", ans2)

from collections import defaultdict

file = open("./year2015/data/day03.txt", "r")
lines = [line.rstrip('\n') for line in file]
mv = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}

G = defaultdict(int)
x, y = 0, 0
G[(x, y)] += 1
for line in lines:
    for c in line:
        x += mv[c][0]
        y += mv[c][1]
        G[(x, y)] += 1
print(len(G))

G = defaultdict(int)
x, y = [0, 0], [0, 0]
G[(x[0], y[0])] += 1
G[(x[1], y[1])] += 1
who = 0
for line in lines:
    for c in line:
        x[who] += mv[c][0]
        y[who] += mv[c][1]
        G[(x[who], y[who])] += 1
        who = 1 - who
print(len(G))

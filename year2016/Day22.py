from collections import namedtuple
import re

Node = namedtuple("Node", ["x", "y", "size", "used", "avail"])

INPUT_FILE = "./year2016/data/day22.txt"


def parse_input(filename):
    nodes = []
    for line in [line.rstrip('\n') for line in open(filename, "r")]:
        p = re.search("/dev/grid/node-x(\\d+)-y(\\d+)\\s*(\\d+)T\\s*(\\d+)T\\s*(\\d+)T", line)
        if p is not None:
            x, y = int(p.group(1)), int(p.group(2))
            size, used, avail = int(p.group(3)), int(p.group(4)), int(p.group(5))
            nodes += [Node(x, y, size, used, avail)]
    return nodes


def list_to_grid(nodes):
    width, height = max([node.x for node in nodes]) + 1, max([node.y for node in nodes]) + 1
    grid = [[Node(0, 0, 0, 0, 0) for _ in range(height)] for _ in range(width)]
    for node in nodes:
        grid[node.x][node.y] = node
    return grid


nodes = parse_input(INPUT_FILE)

ans1 = 0
for a in nodes:
    for b in nodes:
        if a != b and a.used != 0 and a.used <= b.avail:
            ans1 += 1
print("part 1:", ans1)

print()
print("part 2:")

G = list_to_grid(nodes)
W = len(G)
H = len(G[1])
print("width:", W)
print("height:", H)
print("number of nodes:", W * H)

used = [G[x][y].used for x in range(W) for y in range(H)]
used = sorted(used)
print("used sorted:", used)

avail = [G[x][y].avail for x in range(W) for y in range(H)]
avail = sorted(avail, reverse=True)
print("avail sorted desc :", avail)

print("node(s) with zero usage: ", end="")
for y in range(H):
    for x in range(W):
        if G[x][y].used == 0:
            print(G[x][y], end=" ")
print()

print("Grid:")
for y in range(H):
    for x in range(W):
        if (x, y) == (0, 0):
            print("(.)", end="")
        elif (x, y) == (W - 1, 0):
            print(" G ", end="")
        elif G[x][y].used == 0:
            print("(_)", end="")
        elif G[x][y].used <= 93:
            print(" . ", end="")
        else:
            print(" # ", end="")
    print()

print()
print("answer part 2: manual calculation based on grid above")

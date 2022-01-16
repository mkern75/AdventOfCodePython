from utils import load_lines
from collections import defaultdict
from enum import Enum

INPUT_FILE = "./year2017/data/day22.txt"


class State(Enum):
    Clean = 0
    Weakened = 1
    Infected = 2
    Flagged = 3


def load_grid(filename):
    grid = defaultdict(lambda: State.Clean)
    lines = load_lines(filename)
    R, C = len(lines), len(lines[0])
    for r in range(R):
        for c in range(C):
            if lines[r][c] == "#":
                grid[(c - C // 2, R // 2 - r)] = State.Infected
    return grid


grid = load_grid(INPUT_FILE)
x, y, dx, dy = 0, 0, 0, 1
infections = 0
for burst in range(10000):
    if grid[(x, y)] == State.Infected:
        dx, dy = dy, -dx
        grid[(x, y)] = State.Clean
    else:
        dx, dy = -dy, dx
        grid[(x, y)] = State.Infected
        infections += 1
    x, y = x + dx, y + dy
print("part 1:", infections)

grid = load_grid(INPUT_FILE)
x, y, dx, dy = 0, 0, 0, 1
infections = 0
for burst in range(10000000):
    if grid[(x, y)] == State.Clean:
        dx, dy = -dy, dx
        grid[(x, y)] = State.Weakened
    elif grid[(x, y)] == State.Weakened:
        grid[(x, y)] = State.Infected
        infections += 1
    elif grid[(x, y)] == State.Infected:
        dx, dy = dy, -dx
        grid[(x, y)] = State.Flagged
    elif grid[(x, y)] == State.Flagged:
        dx, dy = -dx, -dy
        grid[(x, y)] = State.Clean
    x, y = x + dx, y + dy
print("part 2:", infections)

from utils import load_lines
import re
from colorama import Back, Style

INPUT_FILE = "./year2018/data/day10.txt"


def parse_input(lines):
    points = []
    for line in lines:
        mp = re.compile(r"position=<(.*),(.*)> velocity=<(.*),(.*)>").match(line)
        points += [(int(mp.group(1)), int(mp.group(2)), int(mp.group(3)), int(mp.group(4)))]
    return points


def get_grid(points, t):
    grid = set()
    for point in points:
        grid.add((point[0] + t * point[2], point[1] + t * point[3]))
    return grid


def visualise(grid):
    x_min, x_max = min([x for (x, _) in grid]), max([x for (x, _) in grid])
    y_min, y_max = min([y for (_, y) in grid]), max([y for (_, y) in grid])
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            print(Back.GREEN + "#" + Style.RESET_ALL if (x, y) in grid else ".", end="")
        print()


def has_neighbour(x, y, grid):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) != (0, 0) and (x + dx, y + dy) in grid:
                return True
    return False


def is_candidate(grid):
    for (x, y) in grid:
        if not has_neighbour(x, y, grid):
            return False
    return True


lines = load_lines(INPUT_FILE)
points = parse_input(lines)

t = 0
while True:
    t += 1
    grid = get_grid(points, t)
    if is_candidate(grid):
        print("message:")
        visualise(grid)
        print(f"time: {t}s")
        break

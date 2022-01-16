from utils import load_number
from collections import defaultdict

INPUT_FILE = "./year2017/data/day03.txt"


def n_steps_part1(target):
    n, k = 1, 1
    x, y = 0, 0
    dx, dy = 1, 0
    while True:
        for repeat_twice in range(2):
            for i in range(k):
                x, y, n = x + dx, y + dy, n + 1
                if n == target:
                    return abs(x) + abs(y)
            dx, dy = -dy, dx
        k += 1


def sum_adjacent(x, y, grid):
    s = 0
    for xx in range(x - 1, x + 2):
        for yy in range(y - 1, y + 2):
            if (xx, yy) != (x, y):
                s += grid[(xx, yy)]
    return s


def number_on_spirale_above_target_part2(target):
    spirale = defaultdict(int)
    spirale[(0, 0)] = 1
    k = 1
    x, y = 0, 0
    dx, dy = 1, 0
    while True:
        for repeat_twice in range(2):
            for i in range(k):
                x, y = x + dx, y + dy
                spirale[(x, y)] = sum_adjacent(x, y, spirale)
                if spirale[(x, y)] > target:
                    return spirale[(x, y)]
            dx, dy = -dy, dx
        k += 1


target = load_number(INPUT_FILE)

ans1 = n_steps_part1(target)
print("part 1:", ans1)

ans2 = number_on_spirale_above_target_part2(target)
print("part 2:", ans2)

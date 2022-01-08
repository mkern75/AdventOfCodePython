from utils import load_line, tic, toc
from math import inf
import numpy

INPUT_FILE = "./year2018/data/day11.txt"


def power_level(x, y, serial_number):
    rid = x + 10
    pl = rid * y
    pl += serial_number
    pl *= rid
    hd = (pl // 100) % 10
    pl = hd - 5
    return pl


tic()
serial_number = int(load_line(INPUT_FILE))
N = 300

grid = numpy.zeros((N + 1, N + 1), dtype=int)
for x in range(1, N + 1):
    for y in range(1, N + 1):
        grid[x][y] = power_level(x, y, serial_number)

x_best, y_best, power_best = 1, 1, -inf
for x in range(1, N - 1):
    for y in range(1, N - 1):
        power = numpy.sum(grid[x:x + 3, y:y + 3])
        if power > power_best:
            x_best, y_best, power_best = x, y, power
print(f"part 1: {x_best},{y_best}   ({toc():.3f}s)")

tic()
x_best, y_best, power_best, size_best = 0, 0, -inf, 1
for size in range(1, N + 1):
    for x in range(1, N + 2 - size):
        for y in range(1, N + 2 - size):
            power = numpy.sum(grid[x:x + size, y:y + size])
            if power > power_best:
                x_best, y_best, power_best, size_best = x, y, power, size
print(f"part 2: {x_best},{y_best},{size_best}   ({toc():.3f}s)")

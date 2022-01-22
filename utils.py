import time
import re

UTILS_TIME = time.time()


def tic():
    global UTILS_TIME
    UTILS_TIME = time.time()


def toc():
    global UTILS_TIME
    return time.time() - UTILS_TIME


def load_lines(filename):
    file = open(filename, "r")
    return [line.rstrip('\n') for line in file]


def load_line(filename):
    return load_lines(filename)[0]


def load_words(filename, separator=None):
    words = []
    for line in load_lines(filename):
        words.extend([x for x in line.split(separator)])
    return words


def load_word(filename, separator=None):
    return load_words(filename, separator)[0]


def load_numbers(filename, separator=None):
    numbers = []
    for line in load_lines(filename):
        numbers.extend([int(x) for x in line.split(separator)])
    return numbers


def load_number(filename, separator=None):
    return load_numbers(filename, separator)[0]


def load_grid(filename, separator=None):
    grid = []
    for line in load_lines(filename):
        if separator is not None and separator in line:
            grid += [line.split(separator)]
        else:
            grid += [[c for c in line]]
    return grid


def load_int_grid(filename, separator=None):
    grid = []
    for line in load_lines(filename):
        if separator is not None and separator in line:
            grid += [list(map(int, line.split(separator)))]
        else:
            grid += [[int(c) for c in line]]
    return grid


def load_int_program(filename):
    return load_numbers(filename, ",")


def load_text_blocks(filename):
    blocks, block = [], []
    lines = load_lines(filename)
    for i, line in enumerate(lines):
        if line != "":
            block += [line]
        if line == "" or i == len(lines) - 1:
            if len(block) > 0:
                blocks += [block]
            block = []
    return blocks


def display_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print(grid[r][c], end="")
        print()


def sgn(n):
    return 1 if n > 0 else (-1 if n < 0 else 0)


def manhatten_dist(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])


def is_int(s):
    return re.match(r"^[-+]?\d+$", s) is not None


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

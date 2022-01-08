import time

UTILS_TIME = None


def tic():
    global UTILS_TIME
    UTILS_TIME = time.time()


def toc():
    global UTILS_TIME
    return time.time() - UTILS_TIME


def load_numbers(filename, separator=None):
    numbers = []
    file = open(filename, "r")
    lines = [line.rstrip('\n') for line in file]
    for line in lines:
        numbers.extend([int(x) for x in line.split(separator)])
    return numbers


def load_words(filename, separator=None):
    words = []
    file = open(filename, "r")
    lines = [line.rstrip('\n') for line in file]
    for line in lines:
        words.extend([x for x in line.split(separator)])
    return words


def load_word(filename, separator=None):
    return load_words(filename, separator)[0]


def load_lines(filename):
    file = open(filename, "r")
    return [line.rstrip('\n') for line in file]


def load_line(filename):
    return load_lines(filename)[0]

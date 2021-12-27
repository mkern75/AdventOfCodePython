from collections import namedtuple
import math
import re

INPUT_FILE = "./year2016/data/day15.txt"

Disc = namedtuple("Disc", ["name", "n_positions", "start_position"])


def parse_input(filename):
    discs = []
    for line in [line.rstrip('\n') for line in open(filename, "r")]:
        x = re.search("(Disc #\\d+) has (\\d+) positions; at time=\\d+, it is at position (\\d+).", line)
        discs += [Disc(x.group(1), int(x.group(2)), int(x.group(3)))]
    return discs


def lcm(a, b):
    return a * b // math.gcd(a, b)


discs = parse_input(INPUT_FILE)

t, m = 0, 1
for i in range(len(discs)):
    while (t + (i + 1) + discs[i].start_position) % discs[i].n_positions != 0:
        t += m
    m = lcm(m, discs[i].n_positions)
print("part 1:", t)

discs += [Disc("Disc new", 11, 0)]
t, m = 0, 1
for i in range(len(discs)):
    while (t + (i + 1) + discs[i].start_position) % discs[i].n_positions != 0:
        t += m
    m = lcm(m, discs[i].n_positions)
print("part 2:", t)

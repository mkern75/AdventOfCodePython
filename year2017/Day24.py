from utils import load_lines, tic, toc
from collections import namedtuple

INPUT_FILE = "./year2017/data/day24.txt"

Component = namedtuple("component", "port1 port2")


def build_bridge(port, strength, length, components, used, search_for_longest_bridge=False):
    strength_best, length_best = strength, length
    for i, c in enumerate(components):
        if not used[i] and port in [c.port1, c.port2]:
            port_next = c.port2 if port == c.port1 else c.port1
            used[i] = True
            strength_new, length_new = build_bridge(port_next, strength + c.port1 + c.port2, length + 1, components,
                                                    used, search_for_longest_bridge)
            if search_for_longest_bridge:
                if length_new > length_best or (length_new == length_best and strength_new > strength_best):
                    strength_best, length_best = strength_new, length_new
            else:
                if strength_new > strength_best:
                    strength_best, length_best = strength_new, length_new
            used[i] = False
    return strength_best, length_best


tic()
components = []
for line in load_lines(INPUT_FILE):
    port1, port2 = map(int, line.split("/"))
    components += [Component(port1, port2)]

strength_max, _ = build_bridge(0, 0, 0, components, [False] * len(components), False)
print(f"part 1: {strength_max}  ({toc():.3f}s)")

tic()
strength_max, _ = build_bridge(0, 0, 0, components, [False] * len(components), True)
print(f"part 2: {strength_max}  ({toc():.3f}s)")

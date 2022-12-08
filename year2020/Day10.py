from collections import Counter
from functools import lru_cache

INPUT_FILE = "./year2020/data/day10.txt"
adapters = [int(line.rstrip('\n')) for line in open(INPUT_FILE, "r")]

adapters.sort()
c = Counter(list(adapters[i] - adapters[i - 1] for i in range(1, len(adapters))) + [min(adapters), 3])
print(f"part 1: {c[1] * c[3]}")


@lru_cache(maxsize=None)
def n_ways(curr, goal):
    return 1 if curr + 3 == goal else sum(n_ways(a, goal) for a in adapters if 1 <= a - curr <= 3)


print(f"part 2: {n_ways(0, max(adapters) + 3)}")

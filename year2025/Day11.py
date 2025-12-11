from time import time
from collections import defaultdict
from functools import cache

time_start = time()

INPUT_FILE = "./year2025/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

edges = defaultdict(list)
for line in data:
    src, other = line.split(": ")
    edges[src] = other.split()


@cache
def n_paths(src, dest):
    return 1 if src == dest else sum(n_paths(x, dest) for x in edges[src])


ans1 = n_paths("you", "out")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
ans2 += n_paths("svr", "dac") * n_paths("dac", "fft") * n_paths("fft", "out")
ans2 += n_paths("svr", "fft") * n_paths("fft", "dac") * n_paths("dac", "out")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

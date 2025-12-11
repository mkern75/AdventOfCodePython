from time import time
from collections import defaultdict, Counter

time_start = time()

INPUT_FILE = "./year2025/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

nodes, edges = set(), defaultdict(list)
for line in data:
    src, other = line.split(": ")
    nodes.add(src)
    for dest in other.split():
        nodes.add(dest)
        edges[src].append(dest)

# topological sort Kahn
in_degree = Counter()
for e in edges.values():
    for v in e:
        in_degree[v] += 1
topo_sort = []
stack = [node for node in nodes if in_degree[node] == 0]
while stack:
    v = stack.pop()
    topo_sort += [v]
    for u in edges[v]:
        in_degree[u] -= 1
        if in_degree[u] == 0:
            stack += [u]
assert len(topo_sort) == len(nodes)


def n_paths(src, dest):
    cnt = Counter()
    cnt[src] = 1
    for a in topo_sort:
        for b in edges[a]:
            cnt[b] += cnt[a]
    return cnt[dest]


ans1 = n_paths("you", "out")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
ans2 += n_paths("svr", "dac") * n_paths("dac", "fft") * n_paths("fft", "out")
ans2 += n_paths("svr", "fft") * n_paths("fft", "dac") * n_paths("dac", "out")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

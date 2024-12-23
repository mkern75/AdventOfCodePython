from time import time
from collections import defaultdict

time_start = time()

INPUT_FILE = "./year2024/data/day23.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

graph = defaultdict(set)
for line in data:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)

nodes = set(graph.keys())
nodes_t = {n for n in nodes if n.startswith("t")}
cliques_3t = set()

for node1 in nodes_t:
    for node2 in graph[node1]:
        for node3 in graph[node1]:
            if node3 in graph[node2]:
                cliques_3t.add(tuple(sorted((node1, node2, node3))))

ans1 = len(cliques_3t)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def max_cliques_bron_kerbosch_with_pivot(graph):
    """Bron–Kerbosch algorithm with pivoting for finding all maximal cliques in an undirected graph.
       See: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#With_pivoting"""
    cliques = []
    stack = [(set(), set(graph.keys()), set())]
    while stack:
        r, p, x = stack.pop()
        if not p and not x:
            cliques.append(r)
        else:
            u = None  # pivot
            for v in p:
                if u is None or len(graph[v]) > len(graph[u]):
                    u = v
            pp = [v for v in p if v not in graph[u]]
            while pp:
                v = pp.pop()
                stack += [(r.union({v}), p.intersection(graph[v]), x.intersection(graph[v]))]
                x.add(v)
    return cliques


max_clique = set()
for clique in max_cliques_bron_kerbosch_with_pivot(graph):
    if len(clique) > len(max_clique):
        max_clique = clique

ans2 = ",".join(sorted(max_clique))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

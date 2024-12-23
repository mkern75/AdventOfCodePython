from collections import defaultdict
from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day23.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

graph = defaultdict(set)
for line in data:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)

nodes = list(graph.keys())
nodes_t = [node for node in nodes if node.startswith("t")]

cliques_3t = set()
for node1 in nodes_t:
    for node2 in nodes:
        if node2 == node1 or not node2 in graph[node1]:
            continue
        for node3 in nodes:
            if node3 == node1 or node3 == node2 or not node3 in graph[node1] or not node3 in graph[node2]:
                continue
            cliques_3t.add(tuple(sorted((node1, node2, node3))))

ans1 = len(cliques_3t)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def bron_kerbosch(current_clique, nodes_to_explore, nodes_excluded, graph):
    if not nodes_to_explore and not nodes_excluded:
        yield current_clique
    while nodes_to_explore:
        v = nodes_to_explore.pop()
        yield from bron_kerbosch(
            current_clique.union({v}),
            nodes_to_explore.intersection(graph[v]),
            nodes_excluded.intersection(graph[v]),
            graph
        )
        nodes_excluded.add(v)


cliques_all = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
max_clique = set()
for clique in cliques_all:
    if len(clique) > len(max_clique):
        max_clique = clique

ans2 = ",".join(sorted(max_clique))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

from time import time
import networkx as nx
from itertools import combinations

time_start = time()
# INPUT_FILE = "./year2024/data/day23test.txt"
INPUT_FILE = "./year2024/data/day23.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

graph = nx.Graph()
for line in data:
    a, b = line.split("-")
    graph.add_edge(a, b)

ans1 = 0
for combo3 in combinations(graph.nodes, 3):
    if not any(x.startswith("t") for x in combo3):
        continue
    if not graph.has_edge(combo3[0],combo3[1]):
        continue
    if not graph.has_edge(combo3[0],combo3[2]):
        continue
    if not graph.has_edge(combo3[1],combo3[2]):
        continue
    ans1 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

max_clique = []
for clique in nx.find_cliques(graph):
    if len(clique) > len(max_clique):
        max_clique = clique

ans2 = ",".join(sorted(max_clique))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

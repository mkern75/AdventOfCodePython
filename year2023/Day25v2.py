from collections import defaultdict, Counter
from random import choice

INPUT_FILE = "./year2023/data/day25.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

edges = []
adj = defaultdict(list)
for line in data:
    node1, connections = line.split(": ")
    for node2 in connections.split():
        edges += [tuple(sorted((node1, node2)))]
        adj[node1] += [node2]
        adj[node2] += [node1]


def random_spanning_tree():
    edge = choice(edges)
    spanning_tree = [edge]
    spanning_tree_nodes = {edge[0], edge[1]}
    candidate_edges = [(node, x) for node in spanning_tree_nodes for x in adj[node] if x not in spanning_tree_nodes]
    while len(spanning_tree_nodes) < len(adj):
        edge_new = choice(candidate_edges)
        node_new = edge_new[1]
        spanning_tree += [tuple(sorted(edge_new))]
        spanning_tree_nodes |= {node_new}
        candidate_edges = [edge for edge in candidate_edges if edge[1] != node_new]
        candidate_edges += [(node_new, x) for x in adj[node_new] if x not in spanning_tree_nodes]
    return spanning_tree


cnt = Counter()
for _ in range(1_000):
    spanning_tree = random_spanning_tree()
    for edge in spanning_tree:
        cnt[edge] += 1

edges_to_remove = [x[0] for x in cnt.most_common(3)]

q = [edges[0][0]]
seen = {edges[0][0]}
while q:
    node1 = q.pop()
    for node2 in adj[node1]:
        if node2 not in seen and tuple(sorted((node1, node2))) not in edges_to_remove:
            seen |= {node2}
            q += [node2]

ans1 = len(seen) * (len(adj) - len(seen))
print(f"part 1: {ans1}")

import networkx as nx

INPUT_FILE = "./year2023/data/day25.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

graph = nx.DiGraph()

for line in data:
    component, connections = line.split(": ")
    for other_component in connections.split():
        graph.add_edge(component, other_component, capacity=1.0)
        graph.add_edge(other_component, component, capacity=1.0)

nodes = list(graph.nodes)
n_nodes = len(nodes)

cnt = 1
node1 = nodes[0]
for node2 in nodes[1:]:
    if nx.minimum_cut_value(graph, node1, node2) > 3:
        cnt += 1

ans1 = cnt * (graph.number_of_nodes() - cnt)
print(f"part 1: {ans1}")

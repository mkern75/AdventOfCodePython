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
for node2 in nodes[1:]:
    cut_value, partition = nx.minimum_cut(graph, nodes[0], node2)
    if cut_value == 3:
        ans1 = len(partition[0]) * len(partition[1])
        print(f"part 1: {ans1}")
        break

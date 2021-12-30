import time
import networkx as nx

t0 = time.time()
INPUT_FILE = "./year2017/data/day12.txt"


def load_graph(filename):
    graph = nx.Graph()
    for line in [line.rstrip('\n') for line in open(filename, "r")]:
        fr, to = line.split(" <-> ")
        program = int(fr)
        connected_programs = list(map(int, to.split(", ")))
        for connected_program in connected_programs:
            graph.add_edge(program, connected_program)
    return graph


graph = load_graph(INPUT_FILE)

ans1 = len(nx.node_connected_component(graph, 0))
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = nx.number_connected_components(graph)
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

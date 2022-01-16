from utils import load_lines
import networkx as nx

INPUT_FILE = "./year2017/data/day12.txt"


def load_graph(filename):
    graph = nx.Graph()
    for line in load_lines(filename):
        fr, to = line.split(" <-> ")
        program = int(fr)
        connected_programs = list(map(int, to.split(", ")))
        for connected_program in connected_programs:
            graph.add_edge(program, connected_program)
    return graph


graph = load_graph(INPUT_FILE)

ans1 = len(nx.node_connected_component(graph, 0))
print("part 1:", ans1)

ans2 = nx.number_connected_components(graph)
print("part 2:", ans2)

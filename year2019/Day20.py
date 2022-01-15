from utils import load_lines
import networkx as nx

INPUT_FILE = "./year2019/data/day20.txt"


def load_graph_components(filename):
    data = load_lines(filename)
    R, C = len(data), max([len(l) for l in data])

    edges = []
    for r in range(R):
        for c in range(C):
            if data[r][c] == ".":
                for rn, cn in [(r + 1, c), (r, c + 1)]:
                    if rn < R and c < C:
                        if data[rn][cn] == ".":
                            edges += [((r, c), (rn, cn))]

    portals_inner, portals_outer = {}, {}
    for r in range(R):
        for c in range(C):
            if r + 1 < R and data[r][c].isalpha() and data[r + 1][c].isalpha():
                for rn, cn in [(r + 2, c), (r - 1, c)]:
                    if 0 <= rn < R:
                        if data[rn][cn] == ".":
                            if r == 0 or r == R - 2:
                                portals_outer[data[r][c] + data[r + 1][c]] = (rn, cn)
                            else:
                                portals_inner[data[r][c] + data[r + 1][c]] = (rn, cn)
            elif c + 1 < C and data[r][c].isalpha() and data[r][c + 1].isalpha():
                for rn, cn in [(r, c + 2), (r, c - 1)]:
                    if 0 <= cn < C:
                        if data[rn][cn] == ".":
                            if c == 0 or c == C - 2:
                                portals_outer[data[r][c] + data[r][c + 1]] = (rn, cn)
                            else:
                                portals_inner[data[r][c] + data[r][c + 1]] = (rn, cn)

    return edges, portals_outer, portals_inner


def build_graph(edges, portals_outer, portals_inner):
    source = portals_outer["AA"]
    target = portals_outer["ZZ"]
    graph = nx.Graph()
    for edge in edges:
        graph.add_edge(*edge)
    for p in portals_outer:
        if p not in ["AA", "ZZ"]:
            graph.add_edge(portals_outer[p], portals_inner[p])
    return graph, source, target


def build_recursive_graph(edges, portals_outer, portals_inner, max_depth):
    source = (0, portals_outer["AA"])
    target = (0, portals_outer["ZZ"])
    graph = nx.Graph()
    for depth in range(max_depth):
        for edge in edges:
            graph.add_edge((depth, edge[0]), (depth, edge[1]))
        if depth > 0:
            for p in portals_outer:
                if p not in ["AA", "ZZ"]:
                    graph.add_edge((depth, portals_outer[p]), (depth - 1, portals_inner[p]))
    return graph, source, target


edges, portals_outer, portals_inner = load_graph_components(INPUT_FILE)

graph, source, target = build_graph(edges, portals_outer, portals_inner)
ans1 = nx.shortest_path_length(graph, source, target)
print("part 1:", ans1)

# let's try depth of 100
graph, source, target = build_recursive_graph(edges, portals_outer, portals_inner, 100)
ans2 = nx.shortest_path_length(graph, source, target)
print("part 2:", ans2)
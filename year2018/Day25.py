from utils import load_lines, manhatten_dist
import networkx as nx

INPUT_FILE = "./year2018/data/day25.txt"

points = [list(map(int, line.split(","))) for line in load_lines(INPUT_FILE)]
graph = nx.Graph()
for i in range(len(points)):
    graph.add_node(i)
    for j in range(0, i):
        if manhatten_dist(points[i], points[j]) <= 3:
            graph.add_edge(i, j)
print("part 1:", nx.number_connected_components(graph))

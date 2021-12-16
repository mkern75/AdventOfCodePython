import networkx as nx

file = open("./year2021/data/day15.txt", "r")
lines = [line.rstrip('\n') for line in file]


def build_graph_from_grid(grid):
    graph = nx.DiGraph()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for (rn, cn) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # neighbours
                if 0 <= rn < len(grid) and 0 <= cn < len(grid[0]):
                    graph.add_edge((r, c), (rn, cn), weight=grid[rn][cn])
    return graph


grid = [[int(c) for c in line] for line in lines]
dim = len(grid)
graph = build_graph_from_grid(grid)
res = nx.shortest_path_length(graph, (0, 0), (dim - 1, dim - 1), "weight")
print(res)

grid2 = []
for r in range(5 * dim):
    grid2.append([])
    for c in range(5 * dim):
        grid2[r].append((grid[r % dim][c % dim] + r // dim + c // dim - 1) % 9 + 1)
graph2 = build_graph_from_grid(grid2)
res2 = nx.shortest_path_length(graph2, (0, 0), (5 * dim - 1, 5 * dim - 1), "weight")
print(res2)

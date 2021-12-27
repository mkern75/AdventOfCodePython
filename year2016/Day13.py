import networkx as nx

file = open("./year2016/data/day13.txt", "r")
lines = [line.rstrip('\n') for line in file]


def build_grid(width, height, favourite_number):
    grid = [[False for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            n = x * x + 3 * x + 2 * x * y + y + y * y + favourite_number
            b = bin(n)[2:]
            grid[x][y] = b.count("1") % 2 == 0
    return grid


def build_graph(grid):
    graph = nx.DiGraph()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]:
                graph.add_node((x, y))
                for (xn, yn) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:  # neighbours
                    if 0 <= xn < len(grid) and 0 <= yn < len(grid[0]) and grid[xn][yn]:
                        graph.add_edge((x, y), (xn, yn), weight=1)
    return graph


start = (1, 1)
target = (31, 39)
width = 200  # that should be plenty
height = 200  # that should be plenty
favourite_number = int(lines[0])

grid = build_grid(width, height, favourite_number)
graph = build_graph(grid)
ans1 = nx.shortest_path_length(graph, start, target, "weight")
print("part 1:", ans1)

max_steps = 50
ans2 = 0
for x in range(max(0, start[0] - max_steps), start[0] + max_steps + 1):
    for y in range(max(0, start[1] - max_steps), start[1] + max_steps + 1):
        if (x, y) in nx.nodes(graph) and nx.has_path(graph, start, (x, y)):
            if nx.shortest_path_length(graph, start, (x, y), "weight") <= 50:
                ans2 += 1
print("part 2:", ans2)

from datetime import datetime
import networkx as nx
from itertools import permutations
import math

INPUT_FILE = "./year2016/data/day24.txt"


def load_grid(filename):
    file = open(filename, "r")
    lines = [line.rstrip('\n') for line in file]
    return [[c for c in line] for line in lines]


def build_graph(grid):
    graph = nx.DiGraph()
    locations = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "#":
                if grid[r][c].isdigit():
                    locations[int(grid[r][c])] = (r, c)
                for (rn, cn) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # neighbours
                    if 0 <= rn < len(grid) and 0 <= cn < len(grid[0]) and grid[rn][cn] != "#":
                        graph.add_edge((r, c), (rn, cn), weight=1)
    return graph, locations


def calc_shortest_paths(graph, locations):
    shortest_paths = {}
    for i in locations.keys():
        for j in locations.keys():
            if i != j:
                shortest_paths[(i, j)] = nx.shortest_path_length(graph, locations[i], locations[j], "weight")
    return shortest_paths


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

grid = load_grid(INPUT_FILE)
graph, locations = build_graph(grid)
shortest_path = calc_shortest_paths(graph, locations)

numbers_without_zero = sorted(list(locations.keys()))
numbers_without_zero.remove(0)

min_steps = math.inf
for perm in permutations(numbers_without_zero):
    steps = shortest_path[0, perm[0]]
    for i in range(len(perm) - 1):
        steps += shortest_path[perm[i], perm[i + 1]]
    min_steps = min(min_steps, steps)
print("part 1:", min_steps)

min_steps = math.inf
for perm in permutations(numbers_without_zero):
    steps = shortest_path[0, perm[0]] + shortest_path[perm[-1], 0]
    for i in range(len(perm) - 1):
        steps += shortest_path[perm[i], perm[i + 1]]
    min_steps = min(min_steps, steps)
print("part 2:", min_steps)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

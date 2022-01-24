from utils import load_lines, tic, toc
import re
import networkx as nx
import itertools as it

INPUT_FILE = "./year2018/data/day22.txt"
GEAR_OPTIONS = {0: {"torch", "climbing_gear", "both"}, 1: {"climbing_gear", "neither"}, 2: {"torch", "neither"}}


def load_problem_data(filename):
    lines = load_lines(filename)
    p1 = re.compile(r"depth: (\d+)").match(lines[0])
    p2 = re.compile(r"target: (\d+),(\d+)").match(lines[1])
    return int(p1.group(1)), int(p2.group(2)), int(p2.group(1))  # (row, col) = (y, x)


def calc_erosion_grid(depth, target_row, target_col, n_rows, n_cols):
    erosion_grid = [[-1 for _ in range(n_cols)] for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            if (row, col) == (0, 0) or (row, col) == (target_row, target_col):
                erosion_grid[row][col] = (0 + depth) % 20183
            elif row == 0:
                erosion_grid[row][col] = (col * 16807 + depth) % 20183
            elif col == 0:
                erosion_grid[row][col] = (row * 48271 + depth) % 20183
            else:
                erosion_grid[row][col] = (erosion_grid[row][col - 1] * erosion_grid[row - 1][col] + depth) % 20183
    return erosion_grid


def calc_type_grid(erosion_grid):
    return [[erosion_grid[r][c] % 3 for c in range(len(erosion_grid[r]))] for r in range(len(erosion_grid))]


def calc_risk_level(type_grid, target_row, target_col):
    return sum([type_grid[r][c] for c in range(target_col + 1) for r in range(target_row + 1)])


def calc_shortest_path(type_grid, target_row, target_col):
    graph = nx.Graph()
    for row in range(len(type_grid)):
        for col in range(len(type_grid[0])):

            # gear changes
            for gear_changes in it.combinations(GEAR_OPTIONS[type_grid[row][col]], 2):
                graph.add_edge((row, col, gear_changes[0]), (row, col, gear_changes[1]), weight=7)

            # moves to neighbouring field
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= row + dr < n_rows and 0 <= col + dc < n_cols:
                    for gear in GEAR_OPTIONS[type_grid[row][col]].intersection(
                            GEAR_OPTIONS[type_grid[row + dr][col + dc]]):
                        graph.add_edge((row, col, gear), (row + dr, col + dc, gear), weight=1)

    return nx.shortest_path_length(graph, (0, 0, "torch"), (target_row, target_col, "torch"), "weight")


tic()
depth, target_row, target_col = load_problem_data(INPUT_FILE)

erosion_grid = calc_erosion_grid(depth, target_row, target_col, target_row + 1, target_col + 1)
type_grid = calc_type_grid(erosion_grid)
ans1 = calc_risk_level(type_grid, target_row, target_col)
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
n_rows, n_cols = target_row + 101, target_col + 101  # 100 extra rows / columns should be enough
erosion_grid = calc_erosion_grid(depth, target_row, target_col, n_rows, n_cols)
type_grid = calc_type_grid(erosion_grid)
ans2 = calc_shortest_path(type_grid, target_row, target_col)
print(f"part 2: {ans2}   ({toc():.3f}s)")

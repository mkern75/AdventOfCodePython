from utils import load_int_program
from collections import defaultdict
import networkx as nx
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day15.txt"

MOVES = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
REVERSE = {1: 2, 2: 1, 3: 4, 4: 3}

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)

x_droid, y_droid = 0, 0
x_oxygen, y_oxygen = None, None
grid = defaultdict(lambda: " ")
grid[(x_droid, y_droid)] = "."
graph = nx.DiGraph()


def show_grid():
    x_min, x_max = min(x for x, y in grid if grid[x, y] != " "), max(x for x, y in grid if grid[x, y] != " ")
    y_min, y_max = min(y for x, y in grid if grid[x, y] != " "), max(y for x, y in grid if grid[x, y] != " ")
    for y in range(y_max + 1, y_min - 2, -1):
        for x in range(x_min - 1, x_max + 2):
            if (x, y) == (x_droid, y_droid):
                print("D", end="")
            elif (x, y) == (x_oxygen, y_oxygen):
                print("O", end="")
            else:
                print(grid[(x, y)], end="")
        print()


def exec_move(move):
    global x_droid, y_droid, x_oxygen, y_oxygen
    (dx, dy), rev = MOVES[move], REVERSE[move]
    computer.add_input(move)
    computer.run()
    res = computer.pop_output()
    grid[x_droid + dx, y_droid + dy] = "#" if res == 0 else "."
    if res > 0:
        graph.add_edge((x_droid, y_droid), (x_droid + dx, y_droid + dy), move=move)
        graph.add_edge((x_droid + dx, y_droid + dy), (x_droid, y_droid), move=rev)
        x_droid, y_droid = x_droid + dx, y_droid + dy
        if res == 2:
            x_oxygen, y_oxygen = x_droid, y_droid


def single_move_to_unexplored_pos(x, y):
    for dir, (dx, dy) in MOVES.items():
        if grid[(x + dx, y + dy)] == " ":
            return dir
    return None


def path_to_unexplored_pos(x, y):
    for (tx, ty) in grid:
        if (tx, ty) != (x, y) and grid[tx, ty] == ".":
            if final_move := single_move_to_unexplored_pos(tx, ty):
                path = nx.shortest_path(graph, (x_droid, y_droid), (tx, ty))
                return [graph[path[i]][path[i + 1]]["move"] for i in range(len(path) - 1)] + [final_move]
    return None


queue = []
while True:
    if not queue:
        if move := single_move_to_unexplored_pos(x_droid, y_droid):
            queue.append(move)
        elif path := path_to_unexplored_pos(x_droid, y_droid):
            queue.extend(path)
        else:
            break
    exec_move(queue.pop(0))

res1 = nx.shortest_path_length(graph, (0, 0), (x_oxygen, y_oxygen))
print("part 1:", res1)

res2 = 0
for x, y in grid:
    if grid[x, y] == ".":
        res2 = max(res2, nx.shortest_path_length(graph, (x_oxygen, y_oxygen), (x, y)))
print("part 2:", res2)

# show_grid()

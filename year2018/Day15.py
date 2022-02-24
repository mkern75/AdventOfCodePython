from utils import load_lines
from collections import defaultdict
from copy import deepcopy
import networkx as nx
import math

INPUT_FILE = "./year2018/data/day15.txt"


class Unit:
    def __init__(self, race, row, col, ap=3, hp=200):
        self.race, self.row, self.col, self.ap, self.hp = race, row, col, ap, hp

    def loc(self):
        return self.row, self.col

    def is_next(self, other):
        return abs(self.row - other.row) + abs(self.col - other.col) == 1


def load_data(filename):
    units, grid = [], defaultdict(lambda: "#")
    lines = load_lines(filename)
    for row, line in enumerate(lines):
        for col, field in enumerate(line):
            grid[row, col] = field
            if field in ["E", "G"]:
                units += [Unit(grid[row, col], row, col)]
    return units, grid


def neighbour_locations(loc):
    return [(loc[0] - 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1), (loc[0] + 1, loc[1])]


def build_graph(unit, grid):
    graph = nx.Graph()
    for loc, val in grid.items():
        if loc == unit.loc() or val == ".":
            graph.add_node(loc)
            for neighbour_loc in neighbour_locations(loc):
                if grid[neighbour_loc] == ".":
                    graph.add_edge(loc, neighbour_loc)
    return graph


def get_target_units(current_unit, units):
    return [x for x in units if x.race != current_unit.race and x.hp > 0]


def is_next_to_target_unit(unit, target_units):
    return any([unit.is_next(x) for x in target_units])


def get_in_range_locations(target_units, grid):
    return list(set([loc for t in target_units for loc in neighbour_locations(t.loc()) if grid[loc] == "."]))


def get_reachable_locations(unit, in_range_locations, graph):
    return [loc for loc in in_range_locations if loc in graph.nodes() and nx.has_path(graph, unit.loc(), loc)]


def get_nearest_locations(unit, reachable_locations, graph):
    nearest, dist_min = [], math.inf
    for loc in reachable_locations:
        dist = nx.shortest_path_length(graph, unit.loc(), loc)
        if dist < dist_min:
            nearest, dist_min = [loc], dist
        elif dist == dist_min:
            nearest += [loc]
    return nearest


def get_chosen_location(nearest_locations):
    return min(nearest_locations, key=lambda x: (x[0], x[1])) if len(nearest_locations) > 0 else None


def get_new_location(unit, chosen_loc, graph):
    if chosen_loc is None:
        return unit.loc()
    dist = nx.shortest_path_length(graph, unit.loc(), chosen_loc)
    for loc in neighbour_locations(unit.loc()):
        if loc in graph.nodes():
            if nx.shortest_path_length(graph, loc, chosen_loc) == dist - 1:
                return loc


def move(current_unit, target_units, grid):
    if is_next_to_target_unit(current_unit, target_units):
        return
    graph = build_graph(current_unit, grid)
    in_range_locations = get_in_range_locations(target_units, grid)
    reachable_locations = get_reachable_locations(current_unit, in_range_locations, graph)
    nearest_locations = get_nearest_locations(current_unit, reachable_locations, graph)
    chosen_location = get_chosen_location(nearest_locations)
    grid[current_unit.loc()] = "."
    current_unit.row, current_unit.col = get_new_location(current_unit, chosen_location, graph)
    grid[current_unit.loc()] = current_unit.race


def attack(current_unit, target_units, grid):
    target_units = [x for x in target_units if current_unit.is_next(x)]
    if len(target_units) > 0:
        target_unit = min(target_units, key=lambda x: (x.hp, x.row, x.col))
        target_unit.hp = max(0, target_unit.hp - current_unit.ap)
        if target_unit.hp == 0:
            grid[target_unit.row, target_unit.col] = "."


def combat(units, grid, boost=0):
    n_elves = sum([1 for x in units if x.race == "E"])
    for unit in units:
        if unit.race == "E":
            unit.ap += boost
    rnd = 0
    while True:
        rnd += 1
        units_to_action = sorted(units, key=lambda x: (x.row, x.col))
        while len(units_to_action) > 0:
            current_unit = units_to_action.pop(0)
            target_units = get_target_units(current_unit, units)
            if len(target_units) == 0:
                outcome = (rnd - 1) * sum([unit.hp for unit in units])
                elves_all_survive = n_elves == sum([1 for x in units if x.race == "E" and x.hp > 0])
                return outcome, elves_all_survive
            move(current_unit, target_units, grid)
            attack(current_unit, target_units, grid)
            units_to_action = [unit for unit in units_to_action if unit.hp > 0]
        units = [unit for unit in units if unit.hp > 0]


units, grid = load_data(INPUT_FILE)

outcome, _ = combat(deepcopy(units), deepcopy(grid))
print("part 1:", outcome)

elves_all_survive, boost = False, 0
while not elves_all_survive:
    (outcome, elves_all_survive), boost = combat(deepcopy(units), deepcopy(grid), boost), boost + 1
print("part 2:", outcome)

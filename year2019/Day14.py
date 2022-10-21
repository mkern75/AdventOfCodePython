from utils import load_lines
from collections import namedtuple
import networkx as nx
import math

INPUT_FILE = "./year2019/data/day14.txt"

Quanity = namedtuple("quantity", "chemical amount")
Reaction = namedtuple("reaction", "requires produces")

# load reaction data
reactions = {}
for line in load_lines(INPUT_FILE):
    left, right = line.split(" => ")
    requires = []
    for x in left.split(", "):
        q, c = x.split()
        requires += [Quanity(c, int(q))]
    q, c = right.split()
    produces = Quanity(c, int(q))
    reactions[c] = Reaction(requires, produces)

# topological sort of chemicals
g = nx.DiGraph()
for reaction in reactions.values():
    for req in reaction.requires:
        g.add_edge(req.chemical, reaction.produces.chemical)
chemicals_order = [n for n in nx.topological_sort(g)]


# part 1
def calc_required_ore(fuel=1):
    quantity_required = {chemical: 0 for chemical in chemicals_order}
    quantity_required["FUEL"] = fuel
    for chemical in reversed(chemicals_order[1:]):
        reaction = reactions[chemical]
        f = math.ceil(quantity_required[chemical] / reaction.produces.amount)
        for quantity in reaction.requires:
            quantity_required[quantity.chemical] += f * quantity.amount
    return quantity_required["ORE"]


# part 2: binary search
def calc_possible_fuel(ore):
    fuel = 1
    while calc_required_ore(fuel) <= ore:
        fuel *= 2
    fuel_high, fuel_low = fuel, fuel // 2
    while fuel_high > fuel_low + 1:
        fuel_mid = (fuel_high + fuel_low) // 2
        fuel_high, fuel_low = (fuel_mid, fuel_low) if calc_required_ore(fuel_mid) > ore else (fuel_high, fuel_mid)
    return fuel_low


print("part 1:", calc_required_ore())
print("part 2:", calc_possible_fuel(1000000000000))

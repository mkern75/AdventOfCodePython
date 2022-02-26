from utils import load_line, tic, toc
import networkx as nx
from functools import lru_cache
import sys

sys.setrecursionlimit(1_000_000)
INPUT_FILE = "./year2018/data/day20.txt"
MOVES = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}


def load_route(filename):
    return as_tuple(parse_as_list([c for c in load_line(filename)])[1])


def parse_as_list(l, route=None, is_option=False):
    if l[0] == "^":
        return parse_as_list(l[1:], [], is_option)
    elif l[0] == "$":
        return [], route
    elif l[0] in MOVES:
        if is_option:
            route[-1].append(l[0])
        else:
            route.append(l[0])
        return parse_as_list(l[1:], route, is_option)
    elif l[0] == "(":
        l, sub_soute = parse_as_list(l[1:], [[]], True)
        if is_option:
            route[-1].append(sub_soute)
        else:
            route.append(sub_soute)
        return parse_as_list(l, route, is_option)
    elif l[0] == "|":
        return parse_as_list(l[1:], route + [[]], is_option)
    elif l[0] == ")":
        return l[1:], route


def as_tuple(alist):
    ll = []
    for e in alist:
        ll.append(as_tuple(e) if type(e) == list else e)
    return tuple(ll)


def build_tuple(r1, c1, r2, c2):
    return ((r1, c1), (r2, c2)) if r1 < r2 or (r1 == r2 and c1 <= c2) else ((r2, c2), (r1, c1))


@lru_cache(maxsize=None)
def build_doors(route):
    doors = []
    if len(route) > 0:
        if type(route[0]) == tuple:
            for sub_route in route[0]:
                doors.extend(list(build_doors(sub_route + route[1:])))
        elif route[0] in MOVES:
            dr, dc = MOVES[route[0]]
            doors += [build_tuple(0, 0, dr, dc)]
            for ((r1, c1), (r2, c2)) in build_doors(route[1:]):
                doors += [build_tuple(r1 + dr, c1 + dc, r2 + dr, c2 + dc)]
    return tuple(set(doors))  # convert to set to remove duplicates; convert to tuple to make it immutable for caching


def build_graph(doors):
    graph = nx.Graph()
    for (room1, room2) in doors:
        graph.add_edge(room1, room2)
    return graph


tic()
route = load_route(INPUT_FILE)
doors = build_doors(route)
graph = build_graph(doors)
shortest_paths = nx.single_source_shortest_path(graph, (0, 0))

ans1 = max(len(path) - 1 for path in shortest_paths.values())
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
ans2 = sum(1 for path in shortest_paths.values() if len(path) - 1 >= 1000)
print(f"part 2: {ans2}   ({toc():.3f}s)")

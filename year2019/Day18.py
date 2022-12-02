import networkx as nx
import heapq
from utils import tic, toc

INPUT_FILE = "./year2019/data/day18.txt"


def load_grid(file_name):
    """Load original grid as a dictionary"""
    return {(r, c): field for r, line in enumerate(open(file_name, "r")) for c, field in enumerate(line.rstrip("\n"))}


def get_points_of_interest(grid):
    """Calculate points of interest: entrance(s) + keys + doors"""
    pois = {field: loc for loc, field in grid.items() if field not in ["#", "."]}
    keys = sorted(x for x in pois.keys() if x.islower())
    doors = sorted(x for x in pois.keys() if x.isupper())
    return pois, keys, doors


def get_graph(grid):
    """Establish fully connected graph to facilitate shortest-path calculations"""
    graph = nx.Graph()
    for (r, c), field in grid.items():
        if field != "#":
            for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (rn, cn) in grid and grid[rn, cn] != "#":
                    graph.add_edge((r, c), (rn, cn))
    return graph


def calc_distances(grid, pois):
    """Calculate distances between points of interest - no other POI must be on the path"""
    dist = {}
    graph = get_graph(grid)
    for p1 in pois:
        for p2 in pois:
            if p1 < p2:
                edges = [e for e in graph.edges if not (grid[e[0]] in [".", p1, p2] and grid[e[1]] in [".", p1, p2])]
                graph.remove_edges_from(edges)
                if nx.has_path(graph, pois[p1], pois[p2]):
                    dist[p1, p2] = nx.shortest_path_length(graph, pois[p1], pois[p2])
                    dist[p2, p1] = dist[p1, p2]
                for e in edges:
                    graph.add_edge(e[0], e[1])
    return dist


def update_grid_part_2(grid):
    """Updates the grid for part 2 (uses 1/2/3/4 instead 4x @)"""
    r, c = next((r, c) for r, c in grid if grid[r, c] == "@")
    grid[r - 1, c - 1], grid[r - 1, c + 0], grid[r - 1, c + 1] = "1", "#", "2"
    grid[r + 0, c - 1], grid[r + 0, c + 0], grid[r + 0, c + 1] = "#", "#", "#"
    grid[r + 1, c - 1], grid[r + 1, c + 0], grid[r + 1, c + 1] = "4", "#", "3"
    return grid


def solve(grid):
    """Calculates the fewest number of steps necessary to collect all keys"""
    pois, keys, doors = get_points_of_interest(grid)
    locs = tuple(x for x in pois if x in ["@", "1", "2", "3", "4"])
    dist = calc_distances(grid, pois)

    queue, visited = [(0, locs, ())], set()
    heapq.heapify(queue)

    while True:
        n_steps, locs, keys_found = heapq.heappop(queue)
        if len(keys_found) == len(keys):
            return n_steps
        if (locs, keys_found) not in visited:
            visited.add((locs, keys_found))
            for loc in locs:
                for loc_next in [to for (fr, to) in dist if
                                 fr == loc and not (to in doors and to.lower() not in keys_found)]:
                    n_steps_next = n_steps + dist[loc, loc_next]
                    keys_found_next = keys_found
                    if loc_next in keys and loc_next not in keys_found:
                        keys_found_next = tuple(sorted(keys_found + (loc_next,)))
                    locs_next = tuple(x if x != loc else loc_next for x in locs)
                    heapq.heappush(queue, (n_steps_next, locs_next, keys_found_next))


tic()
grid = load_grid(INPUT_FILE)
print(f"part 1: {solve(grid)}  ({toc():.3f}s)")

tic()
grid = update_grid_part_2(grid)
print(f"part 2: {solve(grid)}  ({toc():.3f}s)")

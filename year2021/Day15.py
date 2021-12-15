from collections import defaultdict
from math import inf as infinity
import heapq

file = open("./year2021/data/day15.txt", "r")
lines = [line.rstrip('\n') for line in file]


# edges = dictionary: node to list of tuples (length-of-edge, connected-node)
def dijkstra(edges, src, dest):
    min_dist = defaultdict(lambda: infinity)
    prev = {}
    min_dist[src] = 0
    queue = [(min_dist[src], src)]  # queue contains tuples (min-dist-to-node, node)
    visited = set()
    while len(queue) > 0:
        dist, node = heapq.heappop(queue)  # priority queue: min-heap
        if node == dest:
            path = [dest]  # construct path from src to dest
            while path[0] != src:
                path = [prev[path[0]]] + path
            return dist, path  # return minimum distance and path from src to dest
        if node not in visited:
            visited.add(node)
            for (conn_dist, conn_node) in edges[node]:  # for all connected nodes
                if conn_node not in visited:
                    if dist + conn_dist < min_dist[conn_node]:
                        min_dist[conn_node] = dist + conn_dist
                        heapq.heappush(queue, (min_dist[conn_node], conn_node))
                        prev[conn_node] = node
    return infinity


def grid_to_edges(grid):
    edges = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for (rn, cn) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # neighbours
                if 0 <= rn < len(grid) and 0 <= cn < len(grid[0]):
                    edges[(r, c)].append((grid[rn][cn], (rn, cn)))
    return edges


G = [[int(c) for c in line] for line in lines]
min_dist, _ = dijkstra(grid_to_edges(G), (0, 0), (len(G) - 1, len(G[0]) - 1))
print(min_dist)

G2 = []
for r in range(5 * len(G)):
    G2.append([])
    for c in range(5 * len(G[0])):
        G2[r].append((G[r % len(G)][c % len(G[0])] + r // len(G) + c // len(G[0]) - 1) % 9 + 1)
min_dist2, _ = dijkstra(grid_to_edges(G2), (0, 0), (len(G2) - 1, len(G2[0]) - 1))
print(min_dist2)

import networkx as nx

INPUT_FILE = "./year2022/data/day12.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])


def height(c):
    return (ord("a") if c == "S" else (ord("z") if c == "E" else ord(c))) - ord("a")


graph = nx.DiGraph()
start = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")
end = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "E")
for r in range(R):
    for c in range(C):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C:
                if height(grid[r + dr][c + dc]) - height(grid[r][c]) <= 1:
                    graph.add_edge((r, c), (r + dr, c + dc))

ans1 = nx.shortest_path_length(graph, start, end)
print(f"part 1: {ans1}")

candidates = [(r, c) for r in range(R) for c in range(C) if grid[r][c] in ["a", "S"]]
ans2 = min(nx.shortest_path_length(graph, s, end) for s in candidates if nx.has_path(graph, s, end))
print(f"part 2: {ans2}")

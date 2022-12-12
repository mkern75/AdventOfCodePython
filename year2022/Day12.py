import networkx as nx

INPUT_FILE = "./year2022/data/day12.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])
rs, cs = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "S")
re, ce = next((r, c) for r in range(R) for c in range(C) if grid[r][c] == "E")
grid[rs][cs], grid[re][ce] = "a", "z"

graph = nx.DiGraph()
for r in range(R):
    for c in range(C):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C:
                if ord(grid[r][c]) + 1 >= ord(grid[r + dr][c + dc]):
                    graph.add_edge((r, c), (r + dr, c + dc))

ans1 = nx.shortest_path_length(graph, (rs, cs), (re, ce))
print(f"part 1: {ans1}")

cand = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == "a"]
ans2 = min(nx.shortest_path_length(graph, start, (re, ce)) for start in cand if nx.has_path(graph, start, (re, ce)))
print(f"part 2: {ans2}")

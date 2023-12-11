INPUT_FILE = "./year2023/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

R, C = len(data), len(data[0])

galaxies = [(r, c) for r in range(R) for c in range(C) if data[r][c] == "#"]
N = len(galaxies)

empty_rows = set(range(R)) - set(r for r, _ in galaxies)
empty_cols = set(range(C)) - set(c for _, c in galaxies)


def calc_sum_shortest_dist(expansion_factor):
    res = 0
    for i in range(N - 1):
        r1, c1 = galaxies[i]
        for j in range(i + 1, N):
            r2, c2 = galaxies[j]
            res += abs(r1 - r2) + abs(c1 - c2)
            res += (expansion_factor - 1) * sum(1 for r in empty_rows if min(r1, r2) < r < max(r1, r2))
            res += (expansion_factor - 1) * sum(1 for c in empty_cols if min(c1, c2) < c < max(c1, c2))
    return res


print(f"part 1: {calc_sum_shortest_dist(2)}")
print(f"part 2: {calc_sum_shortest_dist(1_000_000)}")

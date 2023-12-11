INPUT_FILE = "./year2023/data/day11.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


def solve(image, expansion_factor=1):
    n_rows = len(image)
    n_cols = len(image[0])
    empty_rows = [r for r in range(n_rows) if all(data[r][c] == "." for c in range(n_cols))]
    empty_cols = [c for c in range(n_cols) if all(data[r][c] == "." for r in range(n_rows))]
    galaxies = [(r, c) for r in range(n_rows) for c in range(n_cols) if data[r][c] == "#"]
    n_galaxies = len(galaxies)
    res = 0
    for i in range(n_galaxies - 1):
        r1, c1 = galaxies[i]
        for j in range(i + 1, n_galaxies):
            r2, c2 = galaxies[j]
            res += abs(r1 - r2) + abs(c1 - c2)
            res += (expansion_factor - 1) * sum(1 for r in empty_rows if min(r1, r2) < r < max(r1, r2))
            res += (expansion_factor - 1) * sum(1 for c in empty_cols if min(c1, c2) < c < max(c1, c2))
    return res


print(f"part 1: {solve(data, 2)}")
print(f"part 2: {solve(data, 1_000_000)}")

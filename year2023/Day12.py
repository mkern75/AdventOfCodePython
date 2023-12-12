from functools import lru_cache

INPUT_FILE = "./year2023/data/day12.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


@lru_cache(maxsize=None)
def calc_n_arrangements(springs: str, groups: tuple) -> int:
    sum_groups = sum(groups)
    known = springs.count("#")
    unknown = springs.count("?")

    if known == sum_groups == 0:
        return 1
    if not (known <= sum_groups <= known + unknown):
        return 0

    res = 0
    for i in range(len(springs) - groups[0] + 1):
        if "#" in springs[:i]:
            break
        if "." in springs[i:i + groups[0]]:
            continue
        if i + groups[0] < len(springs) and springs[i + groups[0]] == '#':
            continue
        res += calc_n_arrangements(springs[i + groups[0] + 1:], groups[1:])
    return res


ans1, ans2 = 0, 0

for line in data:
    springs, info = line.split()
    groups = tuple(map(int, info.split(",")))
    ans1 += calc_n_arrangements(springs, groups)
    ans2 += calc_n_arrangements((springs + "?") * 4 + springs, groups * 5)

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

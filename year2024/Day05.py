from time import time
from collections import defaultdict, Counter

time_start = time()
INPUT_FILE = "./year2024/data/day05.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans1, ans2 = 0, 0

order = defaultdict(list)
for line in blocks[0]:
    x, y = map(int, line.split("|"))
    order[x] += [y]


def topological_sort_kahn(a):
    in_degree = Counter()
    for x in a:
        for y in order[x]:
            if y in a:
                in_degree[y] += 1
    res = []
    stack = [x for x in a if in_degree[x] == 0]
    while stack:
        x = stack.pop()
        res += [x]
        for y in order[x]:
            if y in a:
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    stack += [y]
    return res if len(res) == len(a) else None


for line in blocks[1]:
    a = list(map(int, line.split(",")))
    b = topological_sort_kahn(a)
    if a == b:
        ans1 += b[len(b) // 2]
    else:
        ans2 += b[len(b) // 2]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

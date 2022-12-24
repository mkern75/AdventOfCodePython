from functools import lru_cache
from collections import deque

INPUT_FILE = "./year2022/data/day24.txt"

grid = [list(line.strip()) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])

walls = {(r, c) for r in range(R) for c in range(C) if grid[r][c] == "#"}
blizzards = [(r, c, grid[r][c]) for r in range(R) for c in range(C) if grid[r][c] in [">", "<", "v", "^"]]
start = (0, next(c for c in range(C) if (0, c) not in walls))
goal = (R - 1, next(c for c in range(C) if (R - 1, c) not in walls))


@lru_cache(maxsize=None)
def get_blizzards(t):
    if t == 0:
        return blizzards
    blizzards_new = []
    for r, c, d in get_blizzards(t - 1):
        dr, dc = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}[d]
        rn, cn = r + dr, c + dc
        if (rn, cn) in walls:
            if rn == 0:
                rn = R - 2
            elif rn == R - 1:
                rn = 1
            elif cn == 0:
                cn = C - 2
            elif cn == C - 1:
                cn = 1
        blizzards_new += [(rn, cn, d)]
    return blizzards_new


@lru_cache(maxsize=None)
def get_blizzard_locations(t):
    return set((r, c) for r, c, _ in get_blizzards(t))


def find_way_bfs(start, goal, t=0):
    q, v = deque([(start[0], start[1], t)]), set()
    while q:
        r, c, t = q.popleft()
        for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            rn, cn, tn = r + dr, c + dc, t + 1
            if 0 <= rn < R and 0 <= cn < C and (rn, cn) not in walls:
                if (rn, cn) not in get_blizzard_locations(tn):
                    if (rn, cn) == goal:
                        return tn
                    if (rn, cn, tn) not in v:
                        q.append((rn, cn, tn))
                        v.add((rn, cn, tn))


# part 1
t1 = find_way_bfs(start, goal)
print(f"part 1: {t1}")

# part 2
t2 = find_way_bfs(goal, start, t1)
t3 = find_way_bfs(start, goal, t2)
print(f"part 2: {t3}")

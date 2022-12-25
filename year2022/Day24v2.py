from collections import defaultdict, deque

MOVES = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

INPUT_FILE = "./year2022/data/day24.txt"
lines = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

blizzards = defaultdict(set)
for r, line in enumerate(lines[1:-1]):
    for c, field in enumerate(line[1:-1]):
        if field in "v^><":
            blizzards[field].add((r, c))
R, C = len(lines) - 2, len(lines[0]) - 2
start, goal = (-1, 0), (R, C - 1)


def has_blizzard(r, c, t):
    if 0 <= r < R and 0 <= c < C:
        for m, (dr, dc) in MOVES.items():
            if ((r - t * dr) % R, (c - t * dc) % C) in blizzards[m]:
                return True
    return False


def find_way_bfs(start, goal, t=0):
    q, v = deque([(start[0], start[1], t)]), set()
    while q:
        r, c, t = q.popleft()
        for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            rn, cn, tn = r + dr, c + dc, t + 1
            if (rn, cn) in {start, goal} or (0 <= rn < R and 0 <= cn < C):
                if not has_blizzard(rn, cn, tn):
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

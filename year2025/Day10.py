from time import time

INF = 1 << 31

time_start = time()
INPUT_FILE = "./year2025/data/day10.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


class Part1:

    def __init__(self, lights, wirings):
        self.lights = lights
        self.wirings = wirings

    def calc_target(self):
        target = 0
        for i, c in enumerate(self.lights):
            if c == "#":
                target |= 1 << i
        return target

    def calc_ops(self):
        ops = []
        for wiring in self.wirings:
            v = 0
            for button in wiring:
                v |= 1 << button
            ops.append(v)
        return ops

    def solve(self):
        start = 0
        target = self.calc_target()
        ops = self.calc_ops()
        dist = [INF] * (1 << len(self.lights))
        dist[start] = 0
        bfs = [start]
        for state in bfs:
            if state == target:
                return dist[state]
            for op in ops:
                state_next = state ^ op
                if dist[state] + 1 < dist[state_next]:
                    dist[state_next] = dist[state] + 1
                    bfs.append(state_next)
        return INF


ans1 = 0
for line in data:
    comp = line.split()
    lights = list(comp[0][1:-1])
    wirings = [list(map(int, c[1:-1].split(","))) for c in comp[1:-1]]
    ans1 += Part1(lights, wirings).solve()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


class Part2:

    def __init__(self, joltage, wirings):
        self.n_joltages = len(joltage)
        self.joltage = joltage
        self.n_wirings = len(wirings)
        self.wirings = wirings
        self.cnt_wirings_remaining = [[0] * self.n_joltages for _ in range(self.n_wirings + 1)]
        self.res = INF

    def reorder_wirings(self):
        todo = self.wirings[:]
        res = []
        while todo:
            cnt = [0] * self.n_joltages
            for wiring in todo:
                for id in wiring:
                    cnt[id] += 1
            mn = min(x for x in cnt if x > 0)
            id = cnt.index(mn)
            next_wiring = None
            for wiring in todo:
                if id in wiring:
                    if next_wiring is None or len(wiring) > len(next_wiring):
                        next_wiring = wiring
            res.append(next_wiring)
            todo.remove(next_wiring)
        self.wirings = res

    def calc_wiring_remaining_per_id(self):
        for i in range(self.n_wirings - 1, -1, -1):
            for j in range(self.n_joltages):
                self.cnt_wirings_remaining[i][j] += self.cnt_wirings_remaining[i + 1][j]
            for j in self.wirings[i]:
                self.cnt_wirings_remaining[i][j] += 1

    def solve(self):
        self.reorder_wirings()
        self.calc_wiring_remaining_per_id()
        self.res = INF
        self.optimise(self.joltage)
        return self.res

    def optimise(self, target_remaining, idx_wiring=0, presses_so_far=0):

        if presses_so_far >= self.res:
            return

        if presses_so_far + max(target_remaining) >= self.res:
            return

        if idx_wiring == self.n_wirings:
            if all(x == 0 for x in target_remaining):
                self.res = presses_so_far
            return

        mn, mx = 0, INF
        for id in self.wirings[idx_wiring]:
            mx = min(mx, target_remaining[id])
            if self.cnt_wirings_remaining[idx_wiring][id] == 1:
                mn = max(mn, target_remaining[id])

        if mn > mx:
            return

        for presses in range(mn, mx + 1):
            target_new = target_remaining[:]
            for id in self.wirings[idx_wiring]:
                target_new[id] -= presses
            self.optimise(target_new, idx_wiring + 1, presses_so_far + presses)


ans2 = 0
for line in data:
    comp = line.split()
    joltage = list(map(int, comp[-1][1:-1].split(",")))
    wirings = [list(map(int, c[1:-1].split(","))) for c in comp[1:-1]]
    ans2 += Part2(joltage, wirings).solve()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

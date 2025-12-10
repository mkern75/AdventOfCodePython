from time import time

INF = 1 << 31

time_start = time()
INPUT_FILE = "./year2025/data/day10.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


class Part1:

    def __init__(self, buttons, lights):
        self.lights = lights
        self.buttons = buttons

    def calc_target(self):
        target = 0
        for i, c in enumerate(self.lights):
            if c == "#":
                target |= 1 << i
        return target

    def calc_ops(self):
        ops = []
        for button in self.buttons:
            v = 0
            for id in button:
                v |= 1 << id
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
    buttons = [list(map(int, c[1:-1].split(","))) for c in comp[1:-1]]
    lights = list(comp[0][1:-1])
    ans1 += Part1(buttons, lights).solve()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


class Part2:

    def __init__(self, buttons, joltage):
        self.n_joltages = len(joltage)
        self.joltage = joltage
        self.n_buttons = len(buttons)
        self.buttons = buttons
        self.cnt_buttons_remaining = [[0] * self.n_joltages for _ in range(self.n_buttons + 1)]
        self.res = INF

    def reorder_buttons(self):
        todo = self.buttons[:]
        res = []
        while todo:
            cnt = [0] * self.n_joltages
            for button in todo:
                for id in button:
                    cnt[id] += 1
            mn = min(x for x in cnt if x > 0)
            id = cnt.index(mn)
            next_button = None
            for button in todo:
                if id in button:
                    if next_button is None or len(button) > len(next_button):
                        next_button = button
            res.append(next_button)
            todo.remove(next_button)
        self.buttons = res

    def calc_buttons_remaining_per_id(self):
        for i in range(self.n_buttons - 1, -1, -1):
            for id in range(self.n_joltages):
                self.cnt_buttons_remaining[i][id] += self.cnt_buttons_remaining[i + 1][id]
            for id in self.buttons[i]:
                self.cnt_buttons_remaining[i][id] += 1

    def solve(self):
        self.reorder_buttons()
        self.calc_buttons_remaining_per_id()
        self.res = INF
        self.optimise(self.joltage)
        return self.res

    def optimise(self, target_remaining, idx_button=0, presses_so_far=0):

        if presses_so_far >= self.res:
            return

        if presses_so_far + max(target_remaining) >= self.res:
            return

        if idx_button == self.n_buttons:
            if all(x == 0 for x in target_remaining):
                self.res = presses_so_far
            return

        mn, mx = 0, INF
        for id in self.buttons[idx_button]:
            mx = min(mx, target_remaining[id])
            if self.cnt_buttons_remaining[idx_button][id] == 1:
                mn = max(mn, target_remaining[id])

        if mn > mx:
            return

        for presses in range(mn, mx + 1):
            target_new = target_remaining[:]
            for id in self.buttons[idx_button]:
                target_new[id] -= presses
            self.optimise(target_new, idx_button + 1, presses_so_far + presses)


ans2 = 0
for line in data:
    comp = line.split()
    buttons = [list(map(int, c[1:-1].split(","))) for c in comp[1:-1]]
    joltage = list(map(int, comp[-1][1:-1].split(",")))
    ans2 += Part2(buttons, joltage).solve()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

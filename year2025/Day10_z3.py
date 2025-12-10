from time import time
import z3

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


class Part2Z3:

    def __init__(self, buttons, joltage):
        self.n_joltages = len(joltage)
        self.joltage = joltage
        self.n_buttons = len(buttons)
        self.buttons = buttons

    def solve(self):
        variables = [z3.Int(f"press_{i}") for i in range(self.n_buttons)]
        z3_solver = z3.Optimize()
        z3_solver.minimize(sum(variables))
        for var in variables:
            z3_solver.add(var >= 0)
        for i in range(self.n_joltages):
            z3_solver.add(sum(var for j, var in enumerate(variables) if i in self.buttons[j]) == self.joltage[i])

        res = z3_solver.check()
        assert res == z3.sat

        model = z3_solver.model()
        return sum(model[v].as_long() for v in variables)


ans2 = 0
for line in data:
    comp = line.split()
    buttons = [list(map(int, c[1:-1].split(","))) for c in comp[1:-1]]
    joltage = list(map(int, comp[-1][1:-1].split(",")))
    ans2 += Part2Z3(buttons, joltage).solve()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

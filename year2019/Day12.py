from utils import load_lines, tic, toc
import re
from itertools import combinations
from math import lcm

INPUT_FILE = "./year2019/data/day12.txt"


def load_moons(filename):
    moons = []
    for line in load_lines(filename):
        mp = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>").match(line)
        moons += [Moon(int(mp.group(1)), int(mp.group(2)), int(mp.group(3)))]
    return moons


def sgn(n):
    return 1 if n > 0 else (-1 if n < 0 else 0)


class Moon:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.vx, self.vy, self.vz = 0, 0, 0

    def apply_gravity(self, other_moon):
        self.vx += sgn(other_moon.x - self.x)
        self.vy += sgn(other_moon.y - self.y)
        self.vz += sgn(other_moon.z - self.z)

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def total_energ(self):
        return self.potential_energy() * self.kinetic_energy()


def one_step(moons):
    for moon1, moon2 in combinations(moons, 2):
        moon1.apply_gravity(moon2)
        moon2.apply_gravity(moon1)
    for moon in moons:
        moon.apply_velocity()


tic()
moons = load_moons(INPUT_FILE)
for _ in range(1000):
    one_step(moons)
ans1 = sum([moon.total_energ() for moon in moons])
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
moons = load_moons(INPUT_FILE)
state_orig = [tuple([(moon.x, moon.vx) for moon in moons])]
state_orig += [tuple([(moon.y, moon.vy) for moon in moons])]
state_orig += [tuple([(moon.z, moon.vz) for moon in moons])]
period = [None] * 3
step = 0
while None in period:
    step += 1
    one_step(moons)
    state = [tuple([(moon.x, moon.vx) for moon in moons])]
    state += [tuple([(moon.y, moon.vy) for moon in moons])]
    state += [tuple([(moon.z, moon.vz) for moon in moons])]
    for i in range(3):
        if period[i] is None and state[i] == state_orig[i]:
            period[i] = step
ans2 = lcm(*period)
print(f"part 2: {ans2}   ({toc():.3f}s)")

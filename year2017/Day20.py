from utils import load_lines
import re
from math import inf
from itertools import combinations

INPUT_FILE = "./year2017/data/day20.txt"


class Particle:
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az):
        self.x, self.y, self.z = x, y, z
        self.vx, self.vy, self.vz = vx, vy, vz
        self.ax, self.ay, self.az = ax, ay, az

    def __repr__(self):
        return f"p=<{self.x},{self.y},{self.z}>, v=<{self.vx},{self.vy},{self.vz}>, a=<{self.ax},{self.ay},{self.az}>"

    def update(self):
        self.vx, self.vy, self.vz = self.vx + self.ax, self.vy + self.ay, self.vz + self.az
        self.x, self.y, self.z = self.x + self.vx, self.y + self.vy, self.z + self.vz

    def collides(self, other_particle):
        return self.x == other_particle.x and self.y == other_particle.y and self.z == other_particle.z


def load_particles(filename):
    particles = []
    for line in load_lines(filename):
        pm = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>").match(
            line)
        x, y, z = int(pm.group(1)), int(pm.group(2)), int(pm.group(3))
        vx, vy, vz = int(pm.group(4)), int(pm.group(5)), int(pm.group(6))
        ax, ay, az = int(pm.group(7)), int(pm.group(8)), int(pm.group(9))
        particles += [Particle(x, y, z, vx, vy, vz, ax, ay, az)]
    return particles


def manhattan_dist(x1, y1, z1, x2=0, y2=0, z2=0):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def update_particles(particles):
    for particle in particles:
        particle.update()
    collisions = set()
    for particle1, particle2 in combinations(particles, 2):
        if particle1.collides(particle2):
            collisions.update([particle1, particle2])
    for particle in collisions:
        particles.remove(particle)


def update_distances(particles, dist):
    moving_apart = True
    for i in range(len(particles) - 1):
        for j in range(i + 1, len(particles)):
            d = manhattan_dist(particles[i].x, particles[i].y, particles[i].z, particles[j].x, particles[j].y,
                               particles[j].z)
            if (i, j) in dist:
                if d <= dist[(i, j)]:
                    moving_apart = False
            dist[(i, j)] = d
    return dist, moving_apart


particles = load_particles(INPUT_FILE)

ans1, min_a = 0, inf
for i, particle in enumerate(particles):
    a = manhattan_dist(particle.ax, particle.ay, particle.az)
    if a < min_a:
        min_a, ans1 = a, i
print("part 1:", ans1)

n_particles, dist = len(particles), {}
dist, _ = update_distances(particles, dist)
while True:
    update_particles(particles)
    dist, moving_apart = update_distances(particles, dist)
    if len(particles) == n_particles and moving_apart:
        break
    n_particles = len(particles)
print("part 2:", len(particles))

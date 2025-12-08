from time import time

time_start = time()


class DisjointSetUnion:
    def __init__(self, n):
        self._parent = list(range(n))
        self._size = [1] * n
        self._set_count = n

    def find_set(self, x):
        """Finds the representative of the set that x belongs to."""
        parent = self._parent
        xx = x
        while x != parent[x]:
            x = parent[x]
        while xx != x:
            parent[xx], xx = x, parent[xx]
        return x

    def same_set(self, x, y):
        """Returns true if x and y belong to the same set, and false otherwise."""
        return self.find_set(x) == self.find_set(y)

    def unite_sets(self, x, y):
        """Unites two sets; returns True if the sets were not united before and False otherwise."""
        x = self.find_set(x)
        y = self.find_set(y)
        if x == y:
            return False
        self._parent[y] = x
        self._size[x] += self._size[y]
        self._set_count -= 1
        return True

    def set_size(self, x):
        """Returns the size of the set that x belongs to."""
        return self._size[self.find_set(x)]

    def n_sets(self):
        """Returns the number of disjoint sets."""
        return self._set_count


INPUT_FILE = "./year2025/data/day08.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

box = [tuple(map(int, line.split(","))) for line in data]
n = len(box)

dist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        d = (box[i][0] - box[j][0]) ** 2 + (box[i][1] - box[j][1]) ** 2 + (box[i][2] - box[j][2]) ** 2
        dist.append((d, i, j))
dist.sort()

ans1, ans2 = 0, 0
dsu = DisjointSetUnion(n)
part1_connections = 1_000
k = 0
while True:
    i, j = dist[k][1:]
    dsu.unite_sets(i, j)
    if dsu.n_sets() == 1:
        ans2 = box[i][0] * box[j][0]
        break
    k += 1
    if k == part1_connections:
        sz = sorted((dsu.set_size(i) for i in range(n) if i == dsu.find_set(i)), reverse=True)
        ans1 = sz[0] * sz[1] * sz[2]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

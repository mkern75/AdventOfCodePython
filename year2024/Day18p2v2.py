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


INPUT_FILE = "./year2024/data/day18.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

byte_pos = [tuple(map(int, line.split(","))) for line in data]

R, C = 71, 71
n = R * C
top, bottom, left, right = n, n + 1, n + 2, n + 3
dsu = DisjointSetUnion(n + 4)


def idx(r, c):
    return r * C + c


obstacle = [False] * n

ans2 = ""
for r, c in byte_pos:
    i = idx(r, c)
    obstacle[i] = True

    if r == 0:
        dsu.unite_sets(i, top)
    if r == R - 1:
        dsu.unite_sets(i, bottom)
    if c == 0:
        dsu.unite_sets(i, left)
    if c == C - 1:
        dsu.unite_sets(i, right)

    for rn, cn in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c + 1),
                   (r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c - 1)]:
        if 0 <= rn < R and 0 <= cn < C:
            j = idx(rn, cn)
            if obstacle[j]:
                dsu.unite_sets(i, j)

    if dsu.same_set(left, top) or dsu.same_set(left, right) or dsu.same_set(bottom, top) or dsu.same_set(bottom, right):
        ans2 = f"{r},{c}"
        break

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

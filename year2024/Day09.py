from time import time
from heapq import heappop, heappush

EMPTY = -1

time_start = time()
# INPUT_FILE = "./year2024/data/day09test.txt"
INPUT_FILE = "./year2024/data/day09.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

disk_map = list(map(int, list(data[0])))

disk = []
free = 0
for pos, x in enumerate(disk_map):
    disk += [EMPTY if pos & 1 else pos >> 1] * x
    free += x if pos & 1 else 0

idx_empty = 0
while free:
    x = disk.pop()
    if x != EMPTY:
        idx_empty = next(i for i in range(idx_empty, len(disk)) if disk[i] == EMPTY)
        disk[idx_empty] = x
    free -= 1

ans1 = sum(i * x for i, x in enumerate(disk))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

disk = {}
free_pq = [[] for _ in range(10)]
pos = 0
id_max = -1
for i, sz in enumerate(disk_map):
    if sz:
        if i & 1:
            heappush(free_pq[sz], pos)
        else:
            id = i >> 1
            disk[id] = (pos, sz)
            id_max = id
    pos += sz

for id in range(id_max, -1, -1):
    pos, sz = disk[id]
    pos_free, sz_free = pos + 1, 0
    for i in range(sz, 10):
        if free_pq[i] and free_pq[i][0] < pos_free:
            pos_free = free_pq[i][0]
            sz_free = i
    if pos_free >= pos:
        continue
    disk[id] = (pos_free, sz)
    heappop(free_pq[sz_free])
    if sz_free > sz:
        heappush(free_pq[sz_free - sz], pos_free + sz)

ans2 = 0
for id, (pos, sz) in disk.items():
    for p in range(pos, pos + sz):
        ans2 += id * p
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

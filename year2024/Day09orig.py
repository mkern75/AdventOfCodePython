from time import time

EMPTY = -1

time_start = time()
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

disk = []
for pos, sz in enumerate(disk_map):
    if not sz:
        continue
    if pos & 1:
        disk.append([EMPTY, sz])
    else:
        disk.append([pos >> 1, sz])

max_id = max(id for id, _ in disk)

fidx = len(disk) - 1
for id in range(max_id, -1, -1):
    fidx = next(i for i in range(fidx, -1, -1) if disk[i][0] == id)
    sz = disk[fidx][1]
    k = next((i for i in range(0, fidx) if disk[i][0] == EMPTY and disk[i][1] >= sz), None)
    if k is not None:
        disk[fidx][0] = EMPTY
        if sz == disk[k][1]:
            disk[k][0] = id
        else:
            disk[k][1] -= sz
            disk.insert(k, [id, sz])

ans2 = 0
pos = 0
for id, sz in disk:
    if id != EMPTY:
        for p in range(pos, pos + sz):
            ans2 += id * p
    pos += sz
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

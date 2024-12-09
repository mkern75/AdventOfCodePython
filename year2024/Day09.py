from time import time

EMPTY = -1

time_start = time()
INPUT_FILE = "./year2024/data/day09.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

disk_map = list(map(int, list(data[0])))

disk = []
free = 0
for i, x in enumerate(disk_map):
    disk += [EMPTY if i & 1 else i >> 1] * x
    free += x if i & 1 else 0

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
for i, x in enumerate(disk_map):
    disk += [[EMPTY if i & 1 else i >> 1, x]]
max_id = max(f[0] for f in disk)

idx_file = len(disk) - 1
for id in range(max_id, -1, -1):
    idx_file = next(i for i in range(idx_file, -1, -1) if disk[i][0] == id)
    sz = disk[idx_file][1]
    k = next((i for i in range(0, idx_file) if disk[i][0] == EMPTY and disk[i][1] >= sz), None)
    if k is not None:
        disk[idx_file][0] = EMPTY
        if sz == disk[k][1]:
            disk[k][0] = id
        else:
            disk[k][1] -= sz
            disk.insert(k, [id, sz])

ans2 = 0
i = 0
for id, cnt in disk:
    for _ in range(cnt):
        if id != EMPTY:
            ans2 += id * i
        i += 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

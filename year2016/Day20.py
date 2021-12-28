from datetime import datetime

INPUT_FILE = "./year2016/data/day20.txt"

print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

blacklist = []
for line in lines:
    blacklist += [tuple(map(int, line.split("-")))]

ip_max = -1
stop = False
while not stop:
    stop = True
    for ip_range in blacklist:
        if ip_range[0] <= ip_max < ip_range[1] or ip_range[0] == ip_max + 1:
            ip_max = ip_range[1]
            stop = False
print("part 1:", ip_max + 1)

ip_compressed = set()  # compressed ip ranges
for ip_range in blacklist:
    ip_compressed.update([ip_range[0], ip_range[1] + 1])
ip_compressed = sorted(list(ip_compressed))

n = len(ip_compressed)
excl = [False] * n
for ip_range in blacklist:
    i1 = ip_compressed.index(ip_range[0])
    i2 = ip_compressed.index(ip_range[1] + 1)
    for i in range(i1, i2):
        excl[i] = True

n_incl = 4294967296
for i in range(n - 1):
    if excl[i]:
        n_incl -= ip_compressed[i + 1] - ip_compressed[i]
print("part 2:", n_incl)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

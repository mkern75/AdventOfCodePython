file = open("./year2015/data/day14.txt", "r")
lines = [line.rstrip('\n') for line in file]

D = {}  # name -> [speed, fly_time, rest_time, km, fly/rest, remain_time, points]

for line in lines:
    s = line.split()
    D[s[0]] = [int(s[3]), int(s[6]), int(s[13]), 0, "fly", int(s[6]), 0]

for t in range(1, 2503 + 1):
    for r in D.keys():
        v = D[r]
        mode = v[4]
        remain_time = v[5]
        if remain_time == 0:  # we are switching mode!
            mode = ("rest" if mode == "fly" else "fly")
            remain_time = (v[1] if mode == "fly" else v[2])
        remain_time -= 1
        km = v[3] + (v[0] if mode == "fly" else 0)
        D[r] = [v[0], v[1], v[2], km, mode, remain_time, v[6]]
    best = max([v[3] for v in D.values()])
    for v in D.values():
        if v[3] == best:
            v[6] += 1

print(max([v[3] for v in D.values()]))
print(max([v[6] for v in D.values()]))

import itertools as it

file = open("./year2015/data/day17.txt", "r")
lines = [line.rstrip('\n') for line in file]
container = [int(line) for line in lines]

cnt = 0
for n in range(1, len(container) + 1):
    for c in it.combinations(container, n):
        if sum(list(c)) == 150:
            cnt += 1
print(cnt)

for n in range(1, len(container) + 1):
    cnt = 0
    for c in it.combinations(container, n):
        if sum(list(c)) == 150:
            cnt += 1
    if cnt > 0:
        print(cnt)
        break

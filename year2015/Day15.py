file = open("./year2015/data/day15.txt", "r")
lines = [line.rstrip('\n') for line in file]


def distribute(amount, nparts, alist):
    if len(alist) == nparts - 1:
        return [alist + [amount]]
    else:
        r = []
        for i in range(amount + 1):
            r.extend(distribute(amount - i, nparts, alist + [i]))
        return r


INGR = []
for line in lines:
    s = line.replace(":", "").replace(",", "").split()
    INGR += [[s[0], int(s[2]), int(s[4]), int(s[6]), int(s[8]), int(s[10])]]
N = len(INGR)

best1, best2 = -1e9, -1e9
for mix in distribute(100, N, []):
    score, cal = 1, 0
    for p in range(0, 5):
        prop = 0
        for i in range(N):
            prop += mix[i] * INGR[i][p + 1]
        if p < 4:
            score *= max(prop, 0)
        else:
            cal = prop
    best1 = max(score, best1)
    if cal == 500:
        best2 = max(score, best2)
print(best1)
print(best2)

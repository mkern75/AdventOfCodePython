file = open("./year2015/data/day05.txt", "r")
lines = [line.rstrip('\n') for line in file]


def nice1(w):
    if w.count("a") + w.count("e") + w.count("i") + w.count("o") + w.count("u") < 3:
        return 0
    if "ab" in w or "cd" in w or "pq" in w or "xy" in w:
        return 0
    for i in range(len(w) - 1):
        if w[i] == w[i + 1]:
            return 1
    return 0


def nice2(w):
    b = False
    for i in range(len(w) - 3):
        for j in range(i + 2, len(w) - 1):
            if w[i] == w[j] and w[i + 1] == w[j + 1]:
                b = True
                break
    if not b:
        return 0
    for i in range(len(w) - 2):
        if w[i] == w[i + 2]:
            return 1
    return 0


cnt1, cnt2 = 0, 0
for line in lines:
    cnt1 += nice1(line)
    cnt2 += nice2(line)
print(cnt1)
print(cnt2)

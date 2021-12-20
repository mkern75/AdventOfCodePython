file = open("./year2016/data/day03.txt", "r")
lines = [line.rstrip('\n') for line in file]


def check(ll):
    return 1 if max(ll) < sum(ll) - max(ll) else 0


ans1 = 0
for line in lines:
    ans1 += check(list(map(int, line.split())))
print(ans1)

ans2 = 0
for i in range(len(lines) // 3):
    a = list(map(int, lines[i * 3 + 0].split()))
    b = list(map(int, lines[i * 3 + 1].split()))
    c = list(map(int, lines[i * 3 + 2].split()))
    for j in range(3):
        ans2 += check([a[j], b[j], c[j]])
print(ans2)

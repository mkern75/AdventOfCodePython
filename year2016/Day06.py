from collections import Counter

file = open("./year2016/data/day06.txt", "r")
lines = [line.rstrip('\n') for line in file]

ans1, ans2 = "", ""
N = len(lines[0])
for i in range(N):
    cnt = Counter()
    for line in lines:
        cnt[line[i]] += 1
    print(cnt)
    ans1 += cnt.most_common(1)[0][0]
    ans2 += cnt.most_common()[-1][0]
print(ans1)
print(ans2)
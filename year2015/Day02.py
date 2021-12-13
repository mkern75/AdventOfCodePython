file = open("./year2015/data/day02.txt", "r")
lines = [line.rstrip('\n') for line in file]

paper, ribbon = 0, 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    paper += 2 * (l * w + l * h + w * h) + min(l * w, l * h, w * h)
    ribbon += 2 * (l + w + h - max(l, w, h)) + l * w * h
print(paper)
print(ribbon)

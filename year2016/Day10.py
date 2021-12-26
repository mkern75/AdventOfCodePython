from collections import defaultdict
from copy import copy

file = open("./year2016/data/day10.txt", "r")
lines = [line.rstrip('\n') for line in file]

target = (17, 61)

who = defaultdict(list)
rules = defaultdict(list)
for line in lines:
    s = line.split()
    if s[0] == "value":
        who[s[4] + s[5]] += [int(s[1])]
    elif s[0] == "bot":
        rules[s[0] + s[1]] = [s[5] + s[6], s[10] + s[11]]

ans1, ans2 = None, None

stop = False
while not stop:
    stop = True
    who_tmp = copy(who)  # we can't change a directory while iterating through it
    for bot, values in who.items():
        if bot.startswith("bot") and len(values) == 2:
            low, high = (min(values), max(values))
            if (low, high) == target:
                ans1 = bot[3:]
            if bot in rules:
                trgt_low, trgt_high = rules[bot]
                who_tmp[bot] = []
                who_tmp[trgt_low] += [low]
                who_tmp[trgt_high] += [high]
                stop = False
    who = who_tmp

ans2 = who["output0"][0] * who["output1"][0] * who["output2"][0]

print("part 1:", ans1)
print("part 2:", ans2)

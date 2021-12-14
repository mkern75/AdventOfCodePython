from collections import defaultdict

file = open("./year2021/data/day14.txt", "r")
lines = [line.rstrip('\n') for line in file]

RULES = defaultdict(str)
for i in range(2, len(lines)):
    fr, to = lines[i].split(" -> ")
    RULES[fr] = to

template = lines[0]
PC = defaultdict(int)  # dict: element pair to its count
for i in range(len(template) - 1):
    PC[template[i:i + 2]] += 1

for step in range(1, 41):
    NPC = defaultdict(int)  # new dict for new step
    for pair in PC:
        NPC[pair[0] + RULES[pair]] += PC[pair]
        NPC[RULES[pair] + pair[1]] += PC[pair]
    PC = NPC
    if step in [10, 40]:
        EC = defaultdict(int)  # dict: element to its count
        for pair in PC:
            EC[pair[0]] += PC[pair]
        EC[template[-1]] += 1  # don't forget the very last element
        print(max(EC.values()) - min(EC.values()))

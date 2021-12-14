from collections import Counter

file = open("./year2021/data/day14.txt", "r")
lines = [line.rstrip('\n') for line in file]

R = {}  # dict of the rules
for i in range(2, len(lines)):
    pair, element = lines[i].split(" -> ")
    R[pair] = element

template = lines[0]  # initial polymer template
CP = Counter()  # counter of pairs
for i in range(len(template) - 1):
    CP[template[i:i + 2]] += 1

for step in range(1, 41):
    NCP = Counter()  # new counter of pairs for new step
    for pair in CP:
        NCP[pair[0] + R[pair]] += CP[pair]
        NCP[R[pair] + pair[1]] += CP[pair]
    CP = NCP
    if step in [10, 40]:
        CE = Counter()  # counter of elements
        for pair in CP:
            CE[pair[0]] += CP[pair]
        CE[template[-1]] += 1  # don't forget the very last element
        print(max(CE.values()) - min(CE.values()))

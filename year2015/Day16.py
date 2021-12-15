file = open("./year2015/data/day16.txt", "r")
lines = [line.rstrip('\n') for line in file]

MFCSAM = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5,
          "trees": 3, "cars": 2, "perfumes": 1, }


def check(sue, part2=False):
    for key in sue.keys():
        if part2 and key in ["cats", "trees"]:
            if sue[key] <= MFCSAM[key]:
                return False
        elif part2 and key in ["pomeranians", "goldfish"]:
            if sue[key] >= MFCSAM[key]:
                return False
        elif sue[key] != MFCSAM[key]:
            return False
    return True


SUE = {}
for line in lines:
    d = {}
    a, b = line.split(":", 1)
    n = int(a.split()[1])
    for x in b.split(","):
        k, v = x.split(":")
        d[k.strip()] = int(v.strip())
    SUE[n] = d

for n in SUE.keys():
    if check(SUE[n]):
        print("part 1: ", n)
    if check(SUE[n], True):
        print("part 2: ", n)

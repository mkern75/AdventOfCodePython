from collections import defaultdict
from datetime import datetime

file = open("./year2015/data/day19.txt", "r")
block = file.read().split("\n\n")
RULES_FORWARD = defaultdict(list)
RULES_REVERSE = defaultdict(list)
for line in block[0].strip().split('\n'):
    fr, to = line.split(" => ")
    RULES_FORWARD[fr] += [to]
    RULES_REVERSE[to] += [fr]
MOLECULE_START = block[1].strip()


def one_replacement(molecule):
    res = set()
    for i in range(len(molecule)):
        for rule in RULES_FORWARD:
            if molecule[i:].startswith(rule):
                before = molecule[:i]
                after = molecule[i + len(rule):]
                for replace in RULES_FORWARD[rule]:
                    res.add(before + replace + after)
    return res


def as_list(molecule):
    if len(molecule) == 0:
        return []
    elif len(molecule) == 1:
        return [molecule]
    elif molecule[1].islower():
        return [molecule[0:2]] + as_list(molecule[2:])
    else:
        return [molecule[0:1]] + as_list(molecule[1:])


# based on analysis of structure of rule set; does not compute the actual replacement steps
def calc_length_fabrication(mol):
    if len(mol) == len(RULES_FORWARD["e"][0]):
        return 1

    for i in range(len(mol) - 1):
        if mol[i] not in ['Rn', 'Ar', 'Y'] and mol[i + 1] not in ['Rn', 'Ar', 'Y']:
            return 1 + calc_length_fabrication(mol[:i + 1] + mol[i + 2:])

    for i in range(len(mol) - 3):
        if [mol[i + 1], mol[i + 3]] == ["Rn", "Ar"]:
            if len(set([mol[i], mol[i + 2]]).intersection(set(['Rn', 'Ar', 'Y']))) == 0:
                return 1 + calc_length_fabrication(mol[:i + 1] + mol[i + 4:])

    for i in range(len(mol) - 5):
        if [mol[i + 1], mol[i + 3], mol[i + 5]] == ["Rn", "Y", "Ar"]:
            if len(set([mol[i], mol[i + 2], mol[i + 4]]).intersection(set(['Rn', 'Ar', 'Y']))) == 0:
                return 1 + calc_length_fabrication(mol[:i + 1] + mol[i + 6:])

    for i in range(len(mol) - 7):
        if [mol[i + 1], mol[i + 3], mol[i + 5], mol[i + 7]] == ["Rn", "Y", "Y", "Ar"]:
            if len(set([mol[i], mol[i + 2], mol[i + 4], mol[i + 6]]).intersection(set(['Rn', 'Ar', 'Y']))) == 0:
                return 1 + calc_length_fabrication(mol[:i + 1] + mol[i + 8:])


print("start :", datetime.now().strftime("%H:%M:%S.%f"))
ans1 = len(one_replacement(MOLECULE_START))
print("part 1:", ans1)
ans2 = calc_length_fabrication(as_list(MOLECULE_START))
print("part 2:", ans2)
print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

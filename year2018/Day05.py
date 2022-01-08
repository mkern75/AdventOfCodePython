from utils import load_word

INPUT_FILE = "./year2018/data/day05.txt"


def opp(c):
    return c.lower() if c.isupper() else c.upper()


def react(polymer, to_remove=None):
    p = [c for c in polymer]
    i = 0
    while i < len(p) - 1:
        if p[i] == opp(p[i + 1]):
            p.pop(i)
            p.pop(i)
            i = max(0, i - 1)
        elif to_remove is not None and p[i].lower() == to_remove.lower():
            p.pop(i)
            i = max(0, i - 1)
        else:
            i += 1
    return "".join(p)


polymer = load_word(INPUT_FILE)
print("part 1:", len(react(polymer)))

shortest_length = len(polymer)
for to_remove in list(set(polymer.lower())):
    shortest_length = min(shortest_length, len(react(polymer, to_remove)))
print("part 2:", shortest_length)

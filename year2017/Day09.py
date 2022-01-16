from utils import load_line
from collections import namedtuple

INPUT_FILE = "./year2017/data/day09.txt"

Group = namedtuple("Group", ["sub_groups"])
Garbage = namedtuple("Garbage", ["text"])


def parse(s, pos=0):
    c, pos = s[pos:pos + 1], pos + 1
    if c == "{":
        sub_groups = []
        while s[pos:pos + 1] != "}":
            sub_group, pos = parse(s, pos)
            sub_groups += [sub_group]
            if s[pos:pos + 1] == ",":
                _, pos = s[pos:pos + 1], pos + 1  # read ","
        _, pos = s[pos:pos + 1], pos + 1  # read "}"
        return Group(sub_groups), pos
    elif c == "<":
        garbage, d = c, ""
        while d != ">":
            d, pos = s[pos:pos + 1], pos + 1
            garbage += d
            if d == "!":
                e, pos = s[pos:pos + 1], pos + 1
                garbage += e
        return Garbage(garbage), pos


def load_groups(filename):
    group, _ = parse(load_line(filename))
    return group


def score(group, depth=1):
    s = depth
    for x in group.sub_groups:
        if type(x) == Group:
            s += score(x, depth + 1)
    return s


def count_garbage(groups):
    s = 0
    for x in groups.sub_groups:
        if type(x) == Group:
            s += count_garbage(x)
        elif type(x) == Garbage:
            i = 1  # don't count leading "<"
            while i < len(x.text) - 1:  # don't count trailing ">"
                if x.text[i] == "!":  # don't coun't "!" or cancelled characters
                    i += 2
                else:
                    s += 1
                    i += 1
    return s


groups = load_groups(INPUT_FILE)

ans1 = score(groups)
print("part 1:", ans1)

ans2 = count_garbage(groups)
print("part 2:", ans2)

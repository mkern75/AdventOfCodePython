from math import prod
from copy import deepcopy

INPUT_FILE = "./year2023/data/day19.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

workflows = {"A": ["A"], "R": ["R"]}
for line in blocks[0]:
    wid, rules_info = line.split("{")
    workflows[wid] = []
    for info in rules_info[:-1].split(","):
        if ":" in info:
            before, target_wid = info.split(":")
            workflows[wid] += [(before[0], before[1], int(before[2:]), target_wid)]
        else:
            workflows[wid] += [info]


def count_accepted_combinations(x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max):
    res = 0
    q = [("in", {"x": (x_min, x_max), "m": (m_min, m_max), "a": (a_min, a_max), "s": (s_min, s_max)})]
    while q:
        wid, var_vals = q.pop()
        for rule in workflows[wid]:
            if any(mx < mn for mn, mx in var_vals.values()):
                break
            elif rule == "A":
                res += prod(mx - mn + 1 for mn, mx in var_vals.values())
                break
            elif rule == "R":
                break
            elif rule in workflows:
                q += [(rule, deepcopy(var_vals))]
                break
            elif type(rule) is tuple:
                var, comp, threshold, wid_next = rule
                var_vals_next = deepcopy(var_vals)
                if comp == ">":
                    var_vals_next[var] = (max(threshold + 1, var_vals[var][0]), var_vals[var][1])
                    var_vals[var] = (var_vals[var][0], min(var_vals[var][1], threshold))
                elif comp == "<":
                    var_vals_next[var] = (var_vals[var][0], min(threshold - 1, var_vals[var][1]))
                    var_vals[var] = (max(var_vals[var][0], threshold), var_vals[var][1])
                q += [(wid_next, var_vals_next)]
    return res


ans1 = 0
for line in blocks[1]:
    x, m, a, s = map(lambda y: int(y[2:]), line[1:-1].split(","))
    if count_accepted_combinations(x, x, m, m, a, a, s, s) == 1:
        ans1 += x + m + a + s
print(f"part 1: {ans1}")

ans2 = count_accepted_combinations(1, 4000, 1, 4000, 1, 4000, 1, 4000)
print(f"part 2: {ans2}")
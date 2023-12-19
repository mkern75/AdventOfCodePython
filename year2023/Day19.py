from math import prod
from copy import deepcopy

INPUT_FILE = "./year2023/data/day19.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

# split into 2 blocks
blocks = [[]]
for line in data:
    if line:
        blocks[-1] += [line]
    else:
        blocks += [[]]

# read workflows
workflows = {"A": ["A"], "R": ["R"]}
for line in blocks[0]:
    workflow_name, info = line.split("{")
    workflows[workflow_name] = []
    for descr in info[:-1].split(","):
        if ":" in descr:
            before, target_rule = descr.split(":")
            workflows[workflow_name] += [(before[0], before[1], int(before[2:]), target_rule)]
        else:
            workflows[workflow_name] += [descr]


def count_accepted_combinations(x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max):
    res = 0
    q = [("in", {"x": (x_min, x_max), "m": (m_min, m_max), "a": (a_min, a_max), "s": (s_min, s_max)})]
    while q:
        workflow_name, var_vals = q.pop()

        for rule in workflows[workflow_name]:
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

            elif len(rule) == 4:
                var, comp, threshold, workflow_name_next = rule
                var_vals_next = deepcopy(var_vals)
                if comp == ">":
                    var_vals_next[var] = (max(threshold + 1, var_vals[var][0]), var_vals[var][1])
                    var_vals[var] = (var_vals[var][0], min(var_vals[var][1], threshold))
                elif comp == "<":
                    var_vals_next[var] = (var_vals[var][0], min(threshold - 1, var_vals[var][1]))
                    var_vals[var] = (max(var_vals[var][0], threshold), var_vals[var][1])
                q += [(workflow_name_next, var_vals_next)]
    return res


ans1 = 0
for line in blocks[1]:
    x, m, a, s = map(lambda y: int(y[2:]), line[1:-1].split(","))
    if count_accepted_combinations(x, x, m, m, a, a, s, s) == 1:
        ans1 += x + m + a + s
print(f"part 1: {ans1}")

ans2 = count_accepted_combinations(1, 4000, 1, 4000, 1, 4000, 1, 4000)
print(f"part 2: {ans2}")

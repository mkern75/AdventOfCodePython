import functools
from math import inf
from datetime import datetime

AMPHIPOD_TYPES = ["A", "B", "C", "D"]
AMPHIPOD_ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}


def build_state(setup):
    tmp_list = []
    for i in range(11):
        tmp_list += ["."]
    for i in range(4):
        tmp_list += setup[i]
    return tuple(tmp_list)


def is_goal(state):
    return state == GOAL_STATE


def coord(i):
    if i < 11:
        return 0, i
    return 1 + (i - 11) % M, 2 + (i - 11) // M * 2


def index(r, c):
    if r == 0:
        return c
    return 10 + (c - 2) // 2 * M + r


def get_target(i, state):
    c = 2 + 2 * AMPHIPOD_TYPES.index(state[i])
    for r in range(M, 0, -1):
        if state[index(r, c)] == ".":
            return index(r, c)
        elif state[index(r, c)] != state[i]:
            return None
    return None


def is_final(i, state):  # whether amphipod at index i is already in its final place
    r, c = coord(i)
    if c != 2 + 2 * AMPHIPOD_TYPES.index(state[i]):
        return False
    for rr in range(r + 1, M + 1):
        if state[i] != state[index(rr, c)]:
            return False
    return True


def path_is_free(i, j, state):  # one always in the hallway (row 0), the other in the room section (row 1+)
    ri, ci = coord(i)
    rj, cj = coord(j)
    for c in range(min(ci, cj), max(ci, cj) + 1):
        if (0, c) != (ri, ci):
            if state[index(0, c)] != ".":
                return False
    c = ci if ri > 0 else cj
    for r in range(1, max(ri, rj) + 1):
        if (r, c) != (ri, ci):
            if state[index(r, c)] != ".":
                return False
    return True


def get_new_state(i, j, state):
    tmp_list = list(state)
    tmp = tmp_list[i]
    tmp_list[i] = tmp_list[j]
    tmp_list[j] = tmp
    return tuple(tmp_list)


def dist(i, j):  # one always in the hallway (row 0), the other in the room section (row 1+)
    ri, ci = coord(i)
    rj, cj = coord(j)
    return abs(ri - rj) + abs(ci - cj)


def get_neighbours(state):
    neighbours = []
    for i in range(11):
        if state[i] in AMPHIPOD_TYPES:
            target = get_target(i, state)
            if target is not None:
                if path_is_free(i, target, state):
                    neighbour_state = get_new_state(i, target, state)
                    energy = dist(i, target) * AMPHIPOD_ENERGY[state[i]]
                    neighbours += [(neighbour_state, energy)]
    for i in range(11, 11 + N):
        if state[i] in AMPHIPOD_TYPES and not is_final(i, state):
            for j in range(11):
                if state[j] == "." and j not in [2, 4, 6, 8]:
                    if path_is_free(i, j, state):
                        neighbour_state = get_new_state(i, j, state)
                        energy = dist(i, j) * AMPHIPOD_ENERGY[state[i]]
                        neighbours += [(neighbour_state, energy)]
    return neighbours


@functools.lru_cache(maxsize=None)  # DP!
def organise(state):
    if is_goal(state):
        return 0
    else:
        best = inf
        for neighbour, energy in get_neighbours(state):
            best = min(best, energy + organise(neighbour))
        return best


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

start_setup = [["A", "D"], ["C", "D"], ["B", "A"], ["B", "C"]]  # 18,170
goal_setup = [["A", "A"], ["B", "B"], ["C", "C"], ["D", "D"]]
START_STATE = build_state(start_setup)
GOAL_STATE = build_state(goal_setup)
M = len(start_setup[0])
N = len(start_setup[0]) * 4

ans1 = organise(START_STATE)
print("part 1:", ans1)

start_setup = [["A", "D", "D", "D"], ["C", "C", "B", "D"], ["B", "B", "A", "A"], ["B", "A", "C", "C"]]  # 50,208
goal_setup = [["A", "A", "A", "A"], ["B", "B", "B", "B"], ["C", "C", "C", "C"], ["D", "D", "D", "D"]]
START_STATE = build_state(start_setup)
GOAL_STATE = build_state(goal_setup)
M = len(start_setup[0])
N = len(start_setup[0]) * 4

ans2 = organise(START_STATE)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

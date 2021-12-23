import functools
from copy import deepcopy
from math import inf
from datetime import datetime


def build_rooms():
    rooms = []
    for i in range(4):
        for j in range(M):
            rooms += [(1 + j, 2 + 2 * i)]
    return rooms


def amphipod_type(idx):
    return idx // M


def is_goal(state):
    for i in range(N):
        amph_loc = state[i]
        amph_type = amphipod_type(i)
        if amph_loc not in ROOMS[amph_type * M:(amph_type + 1) * M]:
            return False
    return True


def dist(loc_a, loc_b):
    ra, ca = loc_a
    rb, cb = loc_b
    if ca == cb:
        return abs(ra - rb)
    else:
        return abs(ra) + abs(ca - cb) + abs(rb)


def path_is_free(start, target, state):
    rs, cs = start
    rt, ct = target
    if start in ROOMS and target in HALLWAY:
        for r in range(rs - 1, 0, -1):
            if (r, cs) in state:
                return False
        for c in range(min(cs, ct), max(cs, ct) + 1):
            if (0, c) in state:
                return False
    elif start in HALLWAY and target in ROOMS:
        for c in range(min(cs, ct), max(cs, ct) + 1):
            if c != cs and (0, c) in state:
                return False
        for r in range(1, rt + 1):
            if (r, ct) in state:
                return False
    return True


def get_target_room(amph_type, state):
    for i in range(M - 1, -1, -1):
        target_room = ROOMS[amph_type * M + i]
        if target_room not in state:  # room is free
            return target_room
        else:
            j = state.index(target_room)  # somebody else is still in the rooms - can't move in just yet
            if amphipod_type(j) != amph_type:
                return None
    return None


def get_new_state(i, state, new_loc):
    new_n_moves = deepcopy(state[-1])
    tmp = list(new_n_moves)
    tmp[i] = tmp[i] + 1
    new_n_moves = tuple(tmp)
    new_state = deepcopy(state)
    tmp = list(new_state)
    tmp[i] = new_loc
    tmp[-1] = new_n_moves
    return tuple(tmp)


def get_neighbours(state):
    neighbours = []
    for i in range(N):
        amph_loc = state[i]
        amph_n_moves = state[-1][i]
        amph_type = amphipod_type(i)
        if amph_loc in ROOMS and amph_n_moves == 0:
            for hallway_loc in HALLWAY:  # first move is always from room to hallway
                if path_is_free(amph_loc, hallway_loc, state):
                    neighbour_state = get_new_state(i, state, hallway_loc)
                    energy = dist(amph_loc, hallway_loc) * 10 ** amph_type
                    neighbours += [(neighbour_state, energy)]
        elif amph_loc in HALLWAY and amph_n_moves == 1:
            target_loc = get_target_room(amphipod_type(i), state)  # first mmove is always from hallway to target rooms
            if target_loc is not None:
                if path_is_free(amph_loc, target_loc, state):
                    neighbour_state = get_new_state(i, state, target_loc)
                    energy = dist(amph_loc, target_loc) * 10 ** amph_type
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
HALLWAY = [(0, 0), (0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (0, 10)]  # hallway ( does not change between parts)

N = 8  # number of amphipods
M = N // 4  # number of amphipods per type
ROOMS = build_rooms()  # rooms (does not include the hallway)
start = ((1, 2), (2, 6),  # locations of A amphipods
         (1, 6), (1, 8),  # locations of B amphipods
         (1, 4), (2, 8),  # locations of C amphipods
         (2, 2), (2, 4),  # locations of D amphipods
         (0, 0, 0, 0, 0, 0, 0, 0))  # last element: number of moves per amphipod
ans1 = organise(start)
print("part 1:", ans1)

N = 16  # number of amphipods
M = N // 4  # number of amphipods per type
ROOMS = build_rooms()  # rooms (does not include the hallway)
start = ((1, 2), (3, 6), (4, 6), (2, 8),  # locations of A amphipods
         (3, 4), (1, 6), (2, 6), (1, 8),  # locations of B amphipods
         (1, 4), (2, 4), (3, 8), (4, 8),  # locations of C amphipods
         (2, 2), (3, 2), (4, 2), (4, 4),  # locations of D amphipods
         (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))  # last element: number of moves per amphipod
ans2 = organise(start)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

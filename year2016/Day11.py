from collections import deque
from datetime import datetime

# state representation: tuples of values between 1 and 4
# first element represents the position of the elevator
# following pairs represent positions of corresponding generators and chips

INPUT_FILE = "./year2016/data/day11.txt"
FLOOR = {"first": 1, "second": 2, "third": 3, "fourth": 4}


def parse_input(filename):
    generators, chips = {}, {}
    for line in [line.rstrip('\n') for line in open(filename, "r")]:
        w = line.split()
        for i in range(len(w)):
            if w[i].startswith("generator"):
                generators[w[i - 1]] = FLOOR[w[1]]
            elif w[i].endswith("-compatible"):
                chips[w[i][:-11]] = FLOOR[w[1]]
    start = [1]  # elevator
    for element in sorted(generators.keys()):
        start += [generators[element], chips[element]]
    return tuple(start)


def is_valid_chip(state, chip_pos):
    if state[chip_pos] == state[chip_pos - 1]:  # chip on same floor as its generator
        return True
    for j in range(1, len(state), 2):  # chip on same floor with another generator
        if state[chip_pos] == state[j]:
            return False
    return True


def is_valid(state):
    for chip_pos in range(2, len(state), 2):
        if not is_valid_chip(state, chip_pos):
            return False
    return True


def neighbours(state):
    neighbour_list = []
    elevator = state[0]
    for elevator_next in [elevator + 1, elevator - 1]:
        if 1 <= elevator_next <= 4:
            # elevator plus one item
            for i in range(1, len(state)):
                if state[i] == elevator:
                    neighbour = [x for x in state]
                    neighbour[0] = elevator_next
                    neighbour[i] = elevator_next
                    if is_valid(neighbour):
                        neighbour_list += [tuple(neighbour)]
            # elevator plus two items
            for i in range(1, len(state) - 1):
                for j in range(i + 1, len(state)):
                    if state[i] == state[j] == elevator:
                        neighbour = [x for x in state]
                        neighbour[0] = elevator_next
                        neighbour[i] = elevator_next
                        neighbour[j] = elevator_next
                        if is_valid(neighbour):
                            neighbour_list += [tuple(neighbour)]
    return neighbour_list


def bfs(start, goal):
    queue = deque()
    queue.append((0, start))
    explored = {start}
    while len(queue) > 0:
        n_steps, current = queue.popleft()
        if current == goal:
            return n_steps
        for neighbour in neighbours(current):
            if neighbour not in explored:
                explored.add(neighbour)
                queue.append((n_steps + 1, neighbour))


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

start = parse_input(INPUT_FILE)
goal = tuple([4 for _ in start])
ans1 = bfs(start, goal)
print("part 1:", ans1)

start_2 = tuple([x for x in start] + [1, 1, 1, 1])
goal_2 = tuple([4 for _ in start_2])
ans2 = bfs(start_2, goal_2)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

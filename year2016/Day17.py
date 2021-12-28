from datetime import datetime
import hashlib

INPUT_FILE = "./year2016/data/day17.txt"
OPEN = ["b", "c", "d", "e", "f"]


def check_directions(passcode, path_so_far):
    h = hashlib.md5((passcode + path_so_far).encode("utf-8")).hexdigest()
    return h[0] in OPEN, h[1] in OPEN, h[2] in OPEN, h[3] in OPEN


def find_path(passcode, find_shortest=True):
    queue = [(0, 0, "")]
    longest_path = ""
    while len(queue) > 0:
        (row, col, current_path) = queue.pop(0) if find_shortest else queue.pop()
        if (row, col) == (3, 3):
            if find_shortest:
                return current_path
            elif len(current_path) > len(longest_path):
                longest_path = current_path
            continue
        up, down, left, right = check_directions(passcode, current_path)
        if up and row > 0:
            queue += [(row - 1, col, current_path + "U")]
        if down and row < 3:
            queue += [(row + 1, col, current_path + "D")]
        if left and col > 0:
            queue += [(row, col - 1, current_path + "L")]
        if right and col < 3:
            queue += [(row, col + 1, current_path + "R")]
    return longest_path


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

passcode = lines[0]

print("part 1:", find_path(passcode))
print("part 2:", len(find_path(passcode, False)))

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

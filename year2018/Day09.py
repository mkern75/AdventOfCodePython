from utils import load_line, tic, toc
import re

INPUT_FILE = "./year2018/data/day09.txt"


class Marble:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def insert_after(self, new_marble):
        new_marble.next = self
        new_marble.prev = self.prev
        new_marble.next.prev = new_marble
        new_marble.prev.next = new_marble

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = self.prev = None


def parse_input(s):
    mp = re.compile(r"([0-9]+) players; last marble is worth ([0-9]+) points").match(s)
    return int(mp.group(1)), int(mp.group(2))


def play_one_round(current_marble, value, player, points):
    if value % 23 == 0:
        points[player] += value
        for i in range(6):
            current_marble = current_marble.next
        points[player] += current_marble.next.value
        current_marble.next.remove()
    else:
        current_marble = current_marble.prev
        current_marble.insert_after(Marble(value))
        current_marble = current_marble.prev
    return current_marble, points


def play(n_players, n_marbles):
    current_marble = Marble(0)
    current_marble.next = current_marble.prev = current_marble
    points = [0] * n_players
    for value in range(1, n_marbles + 1):
        current_marble, points = play_one_round(current_marble, value, (value - 1) % n_players, points)
    return points


def high_score(n_players, n_marbles):
    return max(play(n_players, n_marbles))


n_players, n_marbles = parse_input(load_line(INPUT_FILE))

tic()
ans1 = high_score(n_players, n_marbles)
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
ans2 = high_score(n_players, n_marbles * 100)
print(f"part 2: {ans2}   ({toc():.3f}s)")

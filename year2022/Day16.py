import re
from collections import namedtuple, deque

Valve = namedtuple("valve", "vid flow_rate bit connections")

INPUT_FILE = "./year2022/data/day16.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def load_valves(data):
    valves = {}
    for line in data:
        reg = re.match(r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)
        vid, flow_rate, connections = reg.groups()
        valves[vid] = Valve(vid, int(flow_rate), None, connections.split(", "))
    return valves


def distance(valves, vid1, vid2):
    q, v = [(0, vid1)], {vid1}
    while q:
        steps, vid = q.pop(0)
        for vid_next in valves[vid].connections:
            if vid_next not in v:
                if vid_next == vid2:
                    return steps + 1
                q += [(steps + 1, vid_next)]
                v |= {vid_next}


def compress_valves(valves):
    valves_new = {}
    ll = sorted(set(["AA"] + [v.vid for v in valves.values() if v.flow_rate > 0]))
    for i, vid in enumerate(ll):
        connections_new = {vid2: distance(valves, vid, vid2) for vid2 in ll if vid2 != vid}
        valves_new[vid] = Valve(vid, valves[vid].flow_rate, pow(2, i), connections_new)
    return valves_new


def solve(valves, time_max, n_players, open_valves=0):
    queue = deque([(1, "AA", 0, 0, open_valves)])

    score_best = 0
    while queue:
        time, vid, score, pressure, open_valves = queue.pop()

        if time == time_max:
            if n_players > 1:
                score += solve(valves, time_max, n_players - 1, open_valves)
            score_best = max(score_best, score)
            continue

        for vid_next, dist in valves[vid].connections.items():
            if open_valves & valves[vid_next].bit == 0 and valves[vid_next].flow_rate > 0:
                time_next = time + dist + 1  # move plus opening the valve
                if time_next <= time_max:
                    pressure_next = pressure + valves[vid_next].flow_rate
                    score_next = score + dist * pressure + 1 * pressure_next
                    open_valves_next = open_valves | valves[vid_next].bit
                    queue.append((time_next, vid_next, score_next, pressure_next, open_valves_next))
        queue.append((time_max, vid, score + (time_max - time) * pressure, pressure, open_valves))

    return score_best


valves = load_valves(data)
valves = compress_valves(valves)
print(f"part 1: {solve(valves, 30, 1)}")  # PyPy: 0.3s  Python: 0.4s
print(f"part 2: {solve(valves, 26, 2)}")  # PyPy:  74s  Python: 241s

import re
from collections import namedtuple, deque

Valve = namedtuple("valve", "vid flow_rate bit connections")

INPUT_FILE = "./year2022/data/day16.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def load_valves(data):
    valves = {}
    for i, line in enumerate(data):
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
        vid_new = vid
        flow_rate_new = valves[vid].flow_rate
        bit_new = pow(2, i)
        connections_new = {vid2: distance(valves, vid, vid2) for vid2 in ll if vid2 != vid}
        valves_new[vid_new] = Valve(vid_new, flow_rate_new, bit_new, connections_new)
    return valves_new


def solve_part1(valves, T, open_valves=0):
    queue = deque([(1, "AA", 0, 0, open_valves, [])])

    score_best, hist_best = 0, []
    while queue:
        time, vid, score, pressure, open_valves, hist = queue.pop()

        if time == T:
            if score > score_best:
                score_best = score
                hist_best = hist
            continue

        move_available = False
        for vid_next, dist in valves[vid].connections.items():
            if open_valves & valves[vid_next].bit == 0 and valves[vid_next].flow_rate > 0:
                time_next = time + dist + 1  # move plus opening the valve
                if time_next <= T:
                    pressure_next = pressure + valves[vid_next].flow_rate
                    score_next = score + dist * pressure + 1 * pressure_next
                    open_valves_next = open_valves | valves[vid_next].bit
                    hist_next = hist + [vid_next + "/" + str(time_next)]
                    queue.append((time_next, vid_next, score_next, pressure_next, open_valves_next, hist_next))
                    move_available = True
        if not move_available:
            queue.append((time + 1, vid, score + pressure, pressure, open_valves, hist))

    return score_best, hist_best


def solve_part2(valves, T, open_valves=0):
    queue = deque([(1, "AA", 0, 0, open_valves, [])])

    score_best, hist_best = 0, []
    while queue:
        time, vid, score, pressure, open_valves, hist = queue.pop()

        if time == T:
            score_other, hist_other = solve_part1(valves, T, open_valves)
            score_overall = score + score_other
            if score_overall > score_best:
                score_best = score_overall
                hist_best = [tuple(hist), tuple(hist_other)]
            continue

        for vid_next, dist in valves[vid].connections.items():
            if open_valves & valves[vid_next].bit == 0 and valves[vid_next].flow_rate > 0:
                time_next = time + dist + 1  # move plus opening the valve
                if time_next <= T:
                    pressure_next = pressure + valves[vid_next].flow_rate
                    score_next = score + dist * pressure + 1 * pressure_next
                    open_valves_next = open_valves | valves[vid_next].bit
                    hist_next = hist + [vid_next + "/" + str(time_next)]
                    queue.append((time_next, vid_next, score_next, pressure_next, open_valves_next, hist_next))
        queue.append((T, vid, score + (T - time) * pressure, pressure, open_valves, hist))

    return score_best, hist_best


valves = load_valves(data)
valves = compress_valves(valves)
print(f"part 1: {solve_part1(valves, 30)}")  # PyPy: 0.4s  Python: 0.5s
print(f"part 2: {solve_part2(valves, 26)}")  # PyPy: 125s  Python: 337s

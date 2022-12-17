import re
from collections import namedtuple
from functools import lru_cache

Valve = namedtuple("valve", "vid flow_rate bit connections")

INPUT_FILE = "./year2022/data/day16.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

#  load valves
valves = {}
for line in data:
    reg = re.match(r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)
    vid, flow_rate, connections = reg.groups()
    valves[vid] = Valve(vid, int(flow_rate), -1, connections.split(", "))


#  compress network down to those valves with flow rate > 0 plus initial valve AA; calculate distances
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


valves_new = {}
ll = sorted(set(["AA"] + [v.vid for v in valves.values() if v.flow_rate > 0]))
for i, vid in enumerate(ll):
    connections_new = {vid2: distance(valves, vid, vid2) for vid2 in ll if vid2 != vid}
    valves_new[vid] = Valve(vid, valves[vid].flow_rate, pow(2, i - 1) if vid != "AA" else 0, connections_new)
valves = valves_new


# recursive depth first search with DP (idea from other AoC users)
@lru_cache(maxsize=None)
def solve(vid, time_remain, open_valves_bitmask=0):
    score = 0
    for vid_next, dist in valves[vid].connections.items():
        if open_valves_bitmask & valves[vid_next].bit == 0:
            time_remain_next = time_remain - dist - 1
            if time_remain_next >= 0:
                open_valves_bitmask_next = open_valves_bitmask | valves[vid_next].bit
                score_next = solve(vid_next, time_remain_next, open_valves_bitmask_next)
                score = max(score, time_remain_next * valves[vid_next].flow_rate + score_next)
    return score


ans1 = solve("AA", 30, 0)
print(f"part 1: {ans1}")  # PyPy: 1.0s  Python: 0.4s

ans2 = 0
upper = pow(2, len(valves) - 1) - 1  # initial valve "AA" can be ignored and is not considered in the bit mask
for n in range((upper + 1)):
    ans2 = max(ans2, solve("AA", 26, n) + solve("AA", 26, upper - n))
print(f"part 2: {ans2}")  # PyPy: 16s  Python: 17s

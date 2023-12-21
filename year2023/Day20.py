from collections import deque, defaultdict
from math import lcm

INPUT_FILE = "./year2023/data/day20.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

LOW_PULSE, HIGH_PULSE = 0, 1
OFF, ON = 0, 1

modules = set()
module_type = defaultdict(lambda: "-")
outputs = defaultdict(list)
inputs = defaultdict(list)
state = defaultdict(lambda: OFF)
high_inputs = defaultdict(set)

for line in data:
    mid, destinatons = line.split(" -> ")
    if mid[0] in "%&":
        mid, mtype = mid[1:], mid[0]
        module_type[mid] = mtype
    modules |= {mid}
    for dest in destinatons.split(", "):
        modules |= {dest}
        outputs[mid] += [dest]
        inputs[dest] += [mid]

inverters = [mid for mid in modules if module_type[mid] == "&" and len(inputs[mid]) == 1]
inverter_first_low_cycle = {}


def press_button(cycle=0):
    low, high = 0, 0
    q = deque([("button", LOW_PULSE, "broadcaster")])
    while q:
        source, pulse, target = q.popleft()

        if target in inverters and pulse == LOW_PULSE:
            if target not in inverter_first_low_cycle:
                inverter_first_low_cycle[target] = cycle

        if pulse == LOW_PULSE:
            low += 1
        else:
            high += 1

        if target not in outputs:
            continue

        elif module_type[target] == "-":
            for dest_next in outputs[target]:
                q.append((target, pulse, dest_next))

        elif module_type[target] == "%":
            if pulse == LOW_PULSE:
                state[target] = ON if state[target] == OFF else OFF
                pulse_next = LOW_PULSE if state[target] == OFF else HIGH_PULSE
                for dest_next in outputs[target]:
                    q.append((target, pulse_next, dest_next))

        elif module_type[target] == "&":
            if pulse == LOW_PULSE:
                high_inputs[target].discard(source)
            else:
                high_inputs[target].add(source)
            pulse_next = LOW_PULSE if len(high_inputs[target]) == len(inputs[target]) else HIGH_PULSE
            for dest_next in outputs[target]:
                q.append((target, pulse_next, dest_next))

    return low, high


# part 1
low, high = 0, 0
for _ in range(1000):
    delta_low, delta_high = press_button()
    low += delta_low
    high += delta_high
ans1 = low * high
print(f"part 1: {ans1}")

# part 2
state = defaultdict(lambda: OFF)
high_inputs = defaultdict(set)
cycle = 0
while len(inverter_first_low_cycle) < len(inverters):
    cycle += 1
    _, _ = press_button(cycle)
ans2 = lcm(*inverter_first_low_cycle.values())
print(f"part 2: {ans2}")

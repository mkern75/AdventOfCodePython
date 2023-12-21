from collections import deque, defaultdict, Counter
from math import prod

INPUT_FILE = "./year2023/data/day20.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

LOW_PULSE, HIGH_PULSE = 0, 1
ON, OFF = True, False


class Module:
    def __init__(self, module_id, module_type, outputs):
        self.id = module_id
        self.type = module_type
        self.state = OFF
        self.outputs = outputs
        self.inputs = []
        self.input_values = defaultdict(lambda: LOW_PULSE)

    def flip_state(self):
        self.state = not self.state

    def update_input_value(self, source_module_id, pulse):
        self.input_values[source_module_id] = pulse

    def all_inputs_high(self):
        return all(self.input_values[input] == HIGH_PULSE for input in self.inputs)

    def is_inverter(self):
        return self.type == "&" and len(self.inputs) == 1

    def reset(self):
        self.state = OFF
        self.input_values.clear()

    def __repr__(self):
        return f"Module(id={self.id}, type={self.type}, state={self.state}, out={self.outputs},  in={self.inputs})"


# load module information
modules = {}
for line in data:
    module_id, destinatons = line.split(" -> ")
    if module_id[0] in "%&":
        module_id, module_type = module_id[1:], module_id[0]
    else:
        module_type = "-"
    modules[module_id] = Module(module_id, module_type, destinatons.split(", "))

# populate inputs for all modules
for module in modules.values():
    for output in module.outputs:
        if output in modules:
            modules[output].inputs += [module.id]


def press_button(modules_to_observe=()):
    cnt = Counter()
    observations = set()
    q = deque([("button", LOW_PULSE, "broadcaster")])
    while q:
        source, pulse, target = q.popleft()

        # for part 1
        cnt[pulse] += 1

        # for part 2
        if target in modules_to_observe:
            observations |= {(target, pulse)}

        if target not in modules:
            continue

        module = modules[target]
        pulse_next = pulse

        if module.type == "%":
            if pulse == LOW_PULSE:
                module.flip_state()
                pulse_next = HIGH_PULSE if module.state == ON else LOW_PULSE
            elif pulse == HIGH_PULSE:
                continue
        elif module.type == "&":
            module.update_input_value(source, pulse)
            pulse_next = LOW_PULSE if module.all_inputs_high() else HIGH_PULSE

        for target_next in module.outputs:
            q.append((target, pulse_next, target_next))

    return cnt, observations


# part 1
cnt = Counter()
for _ in range(1_000):
    cnt_tmp, _ = press_button()
    cnt += cnt_tmp
ans1 = cnt[LOW_PULSE] * cnt[HIGH_PULSE]
print(f"part 1: {ans1}")

# part 2
# - manual analysis of the modules and their connections shows that we really only have to monitor 4 inverters
# - these 4 inverters feed into the final conjunction module which produces the output rx
# - each of the inverters has a certain period when their input is LOW and thus their output turns HIGH
# - 4 HIGH inputs into the final conjunction module produce the desired LOW output for rx
# - thus find the periods of the 4 inverters separately and then calculate their lcm
for module in modules.values():
    module.reset()
inverters = [mid for mid, module in modules.items() if module.is_inverter()]
first_low_cycle_inverters = {}
cycle = 0
while len(first_low_cycle_inverters) < len(inverters):
    cycle += 1
    _, observations = press_button(inverters)
    for inverter_id in inverters:
        if inverter_id not in first_low_cycle_inverters and (inverter_id, LOW_PULSE) in observations:
            first_low_cycle_inverters[inverter_id] = cycle
ans2 = prod(first_low_cycle_inverters.values())
print(f"part 2: {ans2}")

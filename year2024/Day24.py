from time import time
from collections import defaultdict, Counter
from collections import deque
import operator

time_start = time()

INPUT_FILE = "./year2024/data/day24.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

OPERATORS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

inputs = {}  # x/y inputs
for line in blocks[0]:
    x, y = line.split(": ")
    inputs[x] = int(y)

gates = {}  # gates
edges = defaultdict(list)  # edges/order
for line in blocks[1]:
    left, output_wire = line.split(" -> ")
    wire1, op, wire2 = left.split()
    gates[output_wire] = (wire1, op, wire2)
    edges[wire1] += [output_wire]
    edges[wire2] += [output_wire]

wires = list(inputs.keys()) + list(gates.keys())
z_wires = sorted((wire for wire in wires if wire.startswith("z")), reverse=True)

# topological sort of wires
sorted_wires = []
in_degree = Counter()
for wire in wires:
    for wire_to in edges[wire]:
        in_degree[wire_to] += 1
stack = deque([wire for wire in wires if in_degree[wire] == 0])
while stack:
    wire = stack.popleft()
    sorted_wires += [wire]
    for wire_to in edges[wire]:
        in_degree[wire_to] -= 1
        if in_degree[wire_to] == 0:
            stack.append(wire_to)
assert len(sorted_wires) == len(wires)

# simulate
outputs = {}
for wire in sorted_wires:
    if wire in inputs:
        outputs[wire] = inputs[wire]
    else:
        wire1, op, wire2 = gates[wire]
        outputs[wire] = OPERATORS[op](outputs[wire1], outputs[wire2])
binary_result = "".join(map(str, [outputs[wire] for wire in z_wires]))

ans1 = int(binary_result, 2)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# Part 2:
# For each bit (other than bit 0):
#   x[i]          := input
#   y[i]          := input
#   gate_and[i]   := x[i] AND y[i]
#   gate_xor[i]   := x[i] XOR y[i]
#   gate_z[i]     := gate_xor[i] XOR gate_carry[i-1]
#   gate_tmp[i]   := gate_xor[i] AND gate_carry[i-1]
#   gate_carry[i] := gate_tmp[i] OR gate_and[i]

gate_and = [None] * 45
gate_xor = [None] * 45
gate_z = [None] * 45
gate_tmp = [None] * 45
gate_carry = [None] * 45

swaps = []


def find_rule(wire1, operation, wire2):
    for output_wire, (w1, op, w2) in gates.items():
        if (wire1, operation, wire2) in [(w1, op, w2), (w2, op, w1)]:
            return output_wire
    return None


def swap(wire1, wire2):
    global swaps
    gates[wire1], gates[wire2] = gates[wire2], gates[wire1]
    swaps += [wire1, wire2]
    # print(f"*** Swapping {wire1} and {wire2}; swaps={swaps}.")


# bit 0 (this bit is ok in MY input)
i = 0
x = f"x{str(i).zfill(2)}"
y = f"y{str(i).zfill(2)}"
gate_and[i] = find_rule(x, "AND", y)
gate_xor[i] = find_rule(x, "XOR", y)
gate_z[i] = gate_xor[i]
gate_carry[i] = gate_and[i]
# print(f"bit={i}:  and={gate_and[i]}  xor={gate_xor[i]}  z={gate_z[i]}  tmp={gate_tmp[i]}  carry={gate_carry[i]}")

# The logic below works for MY input.
# For other inputs, additional correction/swap logic might have to be added.
for i in range(1, 45):
    x = f"x{str(i).zfill(2)}"
    y = f"y{str(i).zfill(2)}"
    z = f"z{str(i).zfill(2)}"
    check = True
    while check:
        check = False

        gate_and[i] = find_rule(x, "AND", y)

        gate_xor[i] = find_rule(x, "XOR", y)
        # The xor gate should appear as an input for the z gate.
        w1, op, w2 = gates[z]
        if w1 == gate_carry[i - 1] and w2 != gate_xor[i]:
            swap(w2, gate_xor[i])
            check = True
            continue
        if w2 == gate_carry[i - 1] and w1 != gate_xor[i]:
            swap(w1, gate_xor[i])
            check = True
            continue

        gate_z[i] = find_rule(gate_xor[i], "XOR", gate_carry[i - 1])
        # The output of the z gate should be z.
        if gate_z[i] != z:
            swap(gate_z[i], z)
            check = True
            continue

        gate_tmp[i] = find_rule(gate_xor[i], "AND", gate_carry[i - 1])

        gate_carry[i] = find_rule(gate_tmp[i], "OR", gate_and[i])

        # print(f"bit={i}:  and={gate_and[i]}  xor={gate_xor[i]}  z={gate_z[i]}  tmp={gate_tmp[i]}  carry={gate_carry[i]}")

assert len(swaps) == 8

ans2 = ",".join(sorted(swaps))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

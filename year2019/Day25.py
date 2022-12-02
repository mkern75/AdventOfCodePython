from utils import load_int_program
import itertools as it
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day25.txt"

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)


def action(command=None):
    if command is not None:
        print(f"action: {command}")
        computer.add_ascii_input(command + chr(10))
    computer.run()
    output = computer.get_ascii_output()
    print(output)
    return output


# manually explore and collect items
commands = [None, "south", "west", "north", "south", "east", "north", "north", "take mug", "north", "take food ration",
            "south", "east", "north", "north", "south", "east", "take semiconductor", "east", "west", "west", "south",
            "west", "south", "east", "take ornament", "north", "take coin", "east", "take mutex", "west", "south",
            "east", "take candy cane", "east", "east", "west", "west", "west", "west", "south", "east", "take mouse",
            "south", "inv"]
for command in commands:
    action(command)

# find exact weight
items = ["food ration", "candy cane", "mouse", "mug", "coin", "ornament", "semiconductor", "mutex"]
n = len(items)
for b in it.product([True, False], repeat=n):
    for i in range(n):
        if not b[i]:
            action("drop " + items[i])
    output = action("west")
    if "Analysis complete" in output:
        break
    for i in range(n):
        if not b[i]:
            action("take " + items[i])

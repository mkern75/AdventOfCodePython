from utils import load_lines
import re
from collections import namedtuple, Counter

INPUT_FILE = "./year2017/data/day07.txt"

Program = namedtuple("Program", ["name", "weight", "sub_program_names"])


def parse_input(filename):
    programs = {}
    for line in load_lines(filename):
        m = re.compile(r"^([a-z]+) \(([0-9]+)\)(?: -> )?(.*)$").match(line)
        name = m.group(1)
        weight = int(m.group(2))
        sub_program_names = m.group(3).replace(",", "").split()
        programs[name] = Program(name, weight, sub_program_names)
    return programs


def find_bottom(programs):
    for program in programs.values():
        is_bottom = True
        for other_program in programs.values():
            if program.name in other_program.sub_program_names:
                is_bottom = False
        if is_bottom:
            return program
    return None


def weight_subtower(program_name, programs):
    w = programs[program_name].weight
    for sup_program_name in programs[program_name].sub_program_names:
        w += weight_subtower(sup_program_name, programs)
    return w


def is_balanced_subtower(program_name, programs):
    sub_program_names = programs[program_name].sub_program_names
    if len(sub_program_names) <= 1:
        return True
    w = weight_subtower(sub_program_names[0], programs)
    for i in range(1, len(sub_program_names)):
        if weight_subtower(sub_program_names[i], programs) != w:
            return False
    return True


def find_unbalanced_program(programs):
    for program_name in programs:
        if not is_balanced_subtower(program_name, programs):
            return program_name


def find_corrected_weight(programs):
    program_name = find_unbalanced_program(programs)
    weights = Counter()
    for sub_program_name in programs[program_name].sub_program_names:
        weights[weight_subtower(sub_program_name, programs)] += 1
    (correct_weight, _), (incorrect_weight, _) = weights.most_common(2)
    for sub_program_name in programs[program_name].sub_program_names:
        if weight_subtower(sub_program_name, programs) == incorrect_weight:
            return programs[sub_program_name].weight + correct_weight - incorrect_weight


programs = parse_input(INPUT_FILE)

ans1 = find_bottom(programs).name
print("part 1:", ans1)

ans2 = find_corrected_weight(programs)
print("part 2:", ans2)

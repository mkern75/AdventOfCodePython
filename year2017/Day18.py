from utils import load_lines, tic, toc
from collections import defaultdict, deque

INPUT_FILE = "./year2017/data/day18.txt"


class DuetComputer:
    def __init__(self, program, q_in, q_out, part1_mode=True):
        self.program = [instr.split() for instr in program]
        self.memory = defaultdict(int)
        self.ip = 0  # instruction pointer
        self.q_in = q_in
        self.q_out = q_out
        self.cnt_rcv = 0
        self.cnt_snd = 0
        self.rec_frq = None
        self.part1_mode = part1_mode

    def terminated(self):
        return self.ip < 0 or len(self.program) <= self.ip

    def waiting_for_input(self):
        if self.terminated():
            return False
        return self.program[self.ip][0] == "rcv" and len(self.q_in) == 0

    def value(self, s):
        if s.lstrip("-").isnumeric():
            return int(s)
        return self.memory[s]

    def run(self):
        while not self.terminated() and not self.waiting_for_input():
            self.run_one_instruction()

    def run_one_instruction(self):
        if self.terminated():
            return
        instr = self.program[self.ip]
        if instr[0] == "snd":
            self.q_out.append(self.value(instr[1]))
            self.cnt_snd += 1
            self.ip += 1
        elif instr[0] == "set":
            self.memory[instr[1]] = self.value(instr[2])
            self.ip += 1
        elif instr[0] == "add":
            self.memory[instr[1]] += self.value(instr[2])
            self.ip += 1
        elif instr[0] == "mul":
            self.memory[instr[1]] *= self.value(instr[2])
            self.ip += 1
        elif instr[0] == "mod":
            self.memory[instr[1]] %= self.value(instr[2])
            self.ip += 1
        elif instr[0] == "rcv":
            if self.part1_mode:
                if self.value(instr[1]) != 0:
                    self.rec_frq = self.q_in.popleft()
                self.ip += 1
            else:
                if len(self.q_in) > 0:
                    self.memory[instr[1]] = self.q_in.popleft()
                    self.cnt_rcv += 1
                    self.ip += 1
        elif instr[0] == "jgz":
            if self.value(instr[1]) > 0:
                self.ip += self.value(instr[2])
            else:
                self.ip += 1


tic()
program = [line.rstrip('\n') for line in load_lines(INPUT_FILE)]

q_in_out = deque()
computer = DuetComputer(program, q_in_out, q_in_out, True)
computer.run()
ans1 = computer.rec_frq
print(f"part 1: {ans1}  ({toc():.3f}s)")

tic()
q_in_0, q_in_1 = deque(), deque()
comp0 = DuetComputer(program, q_in_0, q_in_1, False)
comp1 = DuetComputer(program, q_in_1, q_in_0, False)
comp0.memory["p"] = 0
comp1.memory["p"] = 1

while not (comp0.terminated() or comp1.terminated() or (comp0.waiting_for_input() and comp1.waiting_for_input())):
    if not comp0.waiting_for_input():
        comp0.run_one_instruction()
    if not comp1.waiting_for_input():
        comp1.run_one_instruction()
ans2 = comp1.cnt_snd
print(f"part 2: {ans2}  ({toc():.3f}s)")

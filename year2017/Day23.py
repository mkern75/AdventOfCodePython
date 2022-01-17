from utils import load_lines, is_prime

INPUT_FILE = "./year2017/data/day23.txt"


class Computer:
    def __init__(self, program):
        self.program = program
        self.memory = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
        self.ipp = 0  # instruction pointer
        self.multiplications = 0

    def val(self, s):
        if s in "abcdefgh":
            return self.memory[s]
        else:
            return int(s)

    def run(self):
        while 0 <= self.ipp < len(self.program):
            self.run_one_instruction()

    def run_one_instruction(self):
        instr = self.program[self.ipp]
        if instr[0] == "set":
            self.memory[instr[1]] = self.val(instr[2])
            self.ipp += 1
        elif instr[0] == "sub":
            self.memory[instr[1]] -= self.val(instr[2])
            self.ipp += 1
        elif instr[0] == "mul":
            self.memory[instr[1]] *= self.val(instr[2])
            self.ipp += 1
            self.multiplications += 1
        elif instr[0] == "jnz":
            if self.val(instr[1]) != 0:
                self.ipp += self.val(instr[2])
            else:
                self.ipp += 1


program = [instr.split() for instr in load_lines(INPUT_FILE)]
computer = Computer(program)
computer.run()
print("part 1:", computer.multiplications)

# program for part 2 runs too long
# it can be sped up but still runs rather slow - the loop below is much faster
# what it does is counting the numbers that are not prime in a certain range counting up with a certain step size
h = 0
fr = int(program[0][2]) * int(program[4][2]) - int(program[5][2])
to = fr - int(program[7][2])
step = -int(program[30][2])
for b in range(fr, to + 1, step):
    if not is_prime(b):
        h += 1
print("part 2:", h)

class MonorailComputer:
    def __init__(self, program):
        self.program = [instr.split() for instr in program]
        self.memory = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.ipp = 0  # instruction pointer
        self.output = []

    def reset(self, program):
        self.program = [instr.split() for instr in program]
        self.memory = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.ipp = 0  # instruction pointer
        self.output = []

    def val(self, s):
        if s in ["a", "b", "c", "d"]:
            return self.memory[s]
        else:
            return int(s)

    def run(self):
        while 0 <= self.ipp < len(self.program):
            self.run_one_instruction()

    def run_one_instruction(self):
        instr = self.program[self.ipp]
        if instr[0] == "cpy":
            self.memory[instr[2]] = self.val(instr[1])
            self.ipp += 1
        elif instr[0] == "inc":
            self.memory[instr[1]] += 1
            self.ipp += 1
        elif instr[0] == "dec":
            self.memory[instr[1]] -= 1
            self.ipp += 1
        elif instr[0] == "jnz":
            if self.val(instr[1]) != 0:
                self.ipp += self.val(instr[2])
            else:
                self.ipp += 1
        elif instr[0] == "tgl":
            addr = self.ipp + self.val(instr[1])
            if 0 <= addr < len(self.program):
                if len(self.program[addr]) == 2:
                    if self.program[addr][0] == "inc":
                        self.program[addr][0] = "dec"
                    else:
                        self.program[addr][0] = "inc"
                elif len(self.program[addr]) == 3:
                    if self.program[addr][0] == "jnz":
                        self.program[addr][0] = "cpy"
                    else:
                        self.program[addr][0] = "jnz"
            self.ipp += 1
        elif instr[0] == "out":
            self.output += [self.val(instr[1])]
            self.ipp += 1

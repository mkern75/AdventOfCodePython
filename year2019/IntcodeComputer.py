from collections import defaultdict


def mode(pmode, i):
    while i > 1:
        pmode //= 10
        i -= 1
    return pmode % 10


class IntcodeComputer:
    def __init__(self, program):
        self._memory = defaultdict(int)
        for i in range(len(program)):
            self._memory[i] = program[i]
        self._input = []
        self._output = []
        self._ip = 0  # instruction pointer
        self._rb = 0  # relative base
        self._finished = False

    def reset(self, program):
        self._memory = defaultdict(int)
        for i in range(len(program)):
            self._memory[i] = program[i]
        self._input = []
        self._output = []
        self._ip = 0
        self._rb = 0
        self._finished = False

    def set_memory(self, pos, val):
        self._memory[pos] = val

    def get_memory(self, pos):
        return self._memory[pos]

    def __read(self, pmode, ip):
        if pmode == 0:  # position mode
            return self._memory[self._memory[ip]]
        elif pmode == 1:  # immediate mode
            return self._memory[ip]
        elif pmode == 2:  # relative mode
            return self._memory[self._memory[ip] + self._rb]
        else:
            assert False, "unknown parameter mode"

    def __write(self, pmode, ip, v):
        if pmode == 0:  # position mode
            self._memory[self._memory[ip]] = v
        elif pmode == 1:  # immediate mode
            assert False, "no write in immediate mode"
        elif pmode == 2:  # relative mode
            self._memory[self._memory[ip] + self._rb] = v
        else:
            assert False, "unknown parameter mode"

    def add_input(self, inp):
        self._input += [inp]

    def __pop_input(self):
        return self._input.pop(0)

    def has_input(self):
        return len(self._input) > 0

    def __add_output(self, outp):
        self._output += [outp]

    def pop_output(self):
        return self._output.pop(0)

    def pop_last_output(self):
        while len(self._output) > 1:
            self.pop_output()
        return self.pop_output()

    def has_output(self):
        return len(self._output) > 0

    def is_finished(self):
        return self._finished

    def run(self):
        while self._ip in self._memory:
            opcode, pmode = self._memory[self._ip] % 100, self._memory[self._ip] // 100
            if opcode == 1:  # add
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                self.__write(mode(pmode, 3), self._ip + 3, v1 + v2)
                self._ip += 4
            elif opcode == 2:  # multiply
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                self.__write(mode(pmode, 3), self._ip + 3, v1 * v2)
                self._ip += 4
            elif opcode == 3:  # input
                if not self.has_input():
                    break
                self.__write(mode(pmode, 1), self._ip + 1, self.__pop_input())
                self._ip += 2
            elif opcode == 4:  # output
                self.__add_output(self.__read(mode(pmode, 1), self._ip + 1))
                self._ip += 2
            elif opcode == 5:  # jump-if-true
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                if v1 != 0:
                    self._ip = v2
                else:
                    self._ip += 3
            elif opcode == 6:  # jump-if-false
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                if v1 == 0:
                    self._ip = v2
                else:
                    self._ip += 3
            elif opcode == 7:  # less than
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                if v1 < v2:
                    self.__write(mode(pmode, 3), self._ip + 3, 1)
                else:
                    self.__write(mode(pmode, 3), self._ip + 3, 0)
                self._ip += 4
            elif opcode == 8:  # equals
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                v2 = self.__read(mode(pmode, 2), self._ip + 2)
                if v1 == v2:
                    self.__write(mode(pmode, 3), self._ip + 3, 1)
                else:
                    self.__write(mode(pmode, 3), self._ip + 3, 0)
                self._ip += 4
            elif opcode == 9:  # relative base offset
                v1 = self.__read(mode(pmode, 1), self._ip + 1)
                self._rb += v1
                self._ip += 2
            elif opcode == 99:
                self._finished = True
                break
            else:
                assert False, "wrong opcode"

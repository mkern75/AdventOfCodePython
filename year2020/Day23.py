INPUT_FILE = "./year2020/data/day23.txt"
label = [line.rstrip('\n') for line in open(INPUT_FILE, "r")][0]


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value} (->{self.next.value})"


class CupRing:
    def __init__(self, label, size):
        self.size = size
        self.current = Cup(int(label[0]))
        previous = self.current
        for i in range(1, len(label)):
            cup = Cup(int(label[i]))
            previous.next = cup
            previous = cup
        for i in range(len(label) + 1, size + 1):
            cup = Cup(i)
            previous.next = cup
            previous = cup
        previous.next = self.current
        self.cups = [self.current] * (size + 1)
        self.cups[self.current.value] = self.current
        tmp = self.current.next
        while tmp != self.current:
            self.cups[tmp.value] = tmp
            tmp = tmp.next

    def exec_move(self):
        # step 1: remove 3 cups
        cup1 = self.current.next
        cup2 = cup1.next
        cup3 = cup2.next
        self.current.next = cup3.next
        # step 2: find destination cup
        dest_value = self.current.value - 1 if self.current.value > 1 else self.size
        while dest_value in [cup1.value, cup2.value, cup3.value]:
            dest_value = dest_value - 1 if dest_value > 1 else self.size
        dest_cup = self.cups[dest_value]
        # step 3: insert 3 cups after destination cup
        cup3.next = dest_cup.next
        dest_cup.next = cup1
        # step 4: move current cup
        self.current = self.current.next

    def exec_moves(self, n):
        for _ in range(n):
            self.exec_move()

    def sequence(self, start=1):
        s, c = str(start), self.cups[start].next
        while c != self.cups[start]:
            s += str(c.value)
            c = c.next
        return s


ring = CupRing(label, len(label))
ring.exec_moves(100)
print(f"part 1: {ring.sequence()[1:]}")

ring = CupRing(label, 1000000)
ring.exec_moves(10000000)
print(f"part 2: {ring.cups[1].next.value * ring.cups[1].next.next.value}")

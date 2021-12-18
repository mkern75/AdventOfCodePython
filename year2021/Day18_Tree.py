from io import StringIO

file = open("./year2021/data/day18.txt", "r")
lines = [line.rstrip('\n') for line in file]


class Node:  # my very first python class
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def __str__(self):
        if type(self.value) == int:
            return str(self.value)
        return "[" + str(self.left_child) + "," + str(self.right_child) + "]"


def parse_str(s):
    return parse(StringIO(s))[0]


def parse(string_io):
    c = string_io.read(1)
    node = Node()
    if c.isdigit():  # digit
        node.value = int(c)
    else:  # opening bracket
        node.left_child, string_io = parse(string_io)
        string_io.read(1)  # comma
        node.right_child, string_io = parse(string_io)
        node.left_child.parent = node.right_child.parent = node
        string_io.read(1)  # closing bracket
    return node, string_io


def add_left(node, to_add):
    while node.parent is not None and node == node.parent.left_child:
        node = node.parent
    if node.parent is not None:
        node = node.parent.left_child
        while node.value is None:
            node = node.right_child
        node.value += to_add


def add_right(node, to_add):
    while node.parent is not None and node == node.parent.right_child:
        node = node.parent
    if node.parent is not None:
        node = node.parent.right_child
        while node.value is None:
            node = node.left_child
        node.value += to_add


def explode(node, depth=0):
    if node.value is not None:
        return False
    if depth == 4:
        add_left(node, node.left_child.value)
        add_right(node, node.right_child.value)
        node.left_child = node.right_child = None
        node.value = 0
        return True
    if explode(node.left_child, depth + 1):
        return True
    elif explode(node.right_child, depth + 1):
        return True
    else:
        return False


def split(node):
    if node.value is not None:
        if node.value >= 10:
            node.left_child = Node(node.value // 2)
            node.right_child = Node((node.value + 1) // 2)
            node.left_child.parent = node.right_child.parent = node
            node.value = None
            return True
        else:
            return False
    else:
        if split(node.left_child):
            return True
        elif split(node.right_child):
            return True
        else:
            return False


def reduce(node):
    while True:
        has_exploded = explode(node)
        if not has_exploded:
            has_slpit = split(node)
            if not has_slpit:
                break
    return node


# note that a will be changed as a result of the addition
def add(a, b):
    node = Node()
    node.left_child = a
    node.right_child = b
    node.left_child.parent = node.right_child.parent = node
    return reduce(node)


def magnitude(node):
    return node.value if node.value is not None else 3 * magnitude(node.left_child) + 2 * magnitude(node.right_child)


sum_numbers = parse_str(lines[0])
for line in lines[1:]:
    sum_numbers = add(sum_numbers, parse_str(line))
print(magnitude(sum_numbers))

best_magnitude = 0
for line1 in lines:
    for line2 in lines:
        if line1 != line2:
            best_magnitude = max(best_magnitude, magnitude(add(parse_str(line1), parse_str(line2))))
print(best_magnitude)

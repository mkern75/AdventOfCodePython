from utils import load_numbers
from collections import namedtuple

INPUT_FILE = "./year2018/data/day08.txt"
Node = namedtuple("node", "n_children n_metadata children metadata")


def parse_input(int_str, pos=0):
    n_children, pos = int_str[pos], pos + 1
    n_metadata, pos = int_str[pos], pos + 1
    children = []
    for i in range(n_children):
        child, pos = parse_input(int_str, pos)
        children += [child]
    metadata = []
    for i in range(n_metadata):
        md, pos = int_str[pos], pos + 1
        metadata += [md]
    node = Node(n_children, n_metadata, children, metadata)
    return node, pos


def sum_metadata(node):
    return sum(node.metadata) + sum([sum_metadata(child) for child in node.children])


def node_value(node):
    if node.n_children == 0:
        return sum(node.metadata)
    v = 0
    for i in range(node.n_metadata):
        if node.metadata[i]-1 < node.n_children:
            v += node_value(node.children[node.metadata[i]-1])
    return v


nums = load_numbers(INPUT_FILE)

node, _ = parse_input(nums)
ans1 = sum_metadata(node)
print("part 1:", ans1)

ans2 = node_value(node)
print("part 2:", ans2)

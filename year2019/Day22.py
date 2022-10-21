from utils import load_lines
import re

INPUT_FILE = "./year2019/data/day22.txt"
N_CARDS = 10_007


def deal_into_new_stack(stack):
    return stack[::-1]


def cut_cards(stack, n):
    return stack[n:] + stack[:n]


def deal_with_increment(stack, n):
    stack_new, pos = [0] * len(stack), 0
    for card in stack:
        stack_new[pos] = card
        pos = (pos + n) % len(stack)
    return stack_new


stack = [i for i in range(N_CARDS)]
for line in load_lines(INPUT_FILE):
    if line == "deal into new stack":
        stack = deal_into_new_stack(stack)
    elif x := re.search(r"deal with increment (.*)", line):
        n = int(x.groups()[0])
        stack = deal_with_increment(stack, n)
    elif x := re.search(r"cut (.*)", line):
        n = int(x.groups()[0])
        stack = cut_cards(stack, n)

print("part 1:", stack.index(2019))

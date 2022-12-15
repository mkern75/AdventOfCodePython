from functools import cmp_to_key

INPUT_FILE = "./year2022/data/day13.txt"
data = [[line.rstrip('\n') for line in p.splitlines()] for p in open(INPUT_FILE).read().strip().split("\n\n")]


def compare(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    elif type(left) == list and type(right) == list:
        for lelem, relem in zip(left, right):
            if res := compare(lelem, relem):
                return res
        return len(left) - len(right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)


print(f"part 1: {sum(i for i, pairs in enumerate(data, 1) if compare(*map(eval, pairs)) < 0)}")

dividers = [[[2]], [[6]]]
packets = [eval(x) for pair in data for x in pair] + dividers
packets.sort(key=cmp_to_key(compare))
print(f"part 2: {(packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)}")
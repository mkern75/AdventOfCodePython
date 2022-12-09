import re
from itertools import product

INPUT_FILE = "./year2020/data/day14.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def apply_mask(val, mask):
    val_bin = bin(val)[2:].zfill(36)
    return int("".join(val_bin[i] if mask[i] == "X" else mask[i] for i in range(36)), 2)


def get_all_addresses(addr, mask):
    addresses = []
    addr_bin = bin(addr)[2:].zfill(36)
    for p in product(["0", "1"], repeat=mask.count("X")):
        addr_bin_new, c = "", 0
        for i in range(36):
            if mask[i] == "0":
                addr_bin_new += addr_bin[i]
            elif mask[i] == "1":
                addr_bin_new += "1"
            else:
                addr_bin_new += p[c]
                c += 1
        addresses += [int(addr_bin_new, 2)]
    return addresses


mem1, mem2, mask = {}, {}, ""
for line in data:
    if reg := re.match(r"mask = ([01X]+)", line):
        mask = reg.groups()[0]
    elif reg := re.match(r"mem\[(\d+)\] = (\d+)", line):
        addr, val = map(int, reg.groups())
        mem1[addr] = apply_mask(val, mask)
        mem2.update({a: val for a in get_all_addresses(addr, mask)})
print(f"part 1: {sum(v for v in mem1.values())}")
print(f"part 2: {sum(v for v in mem2.values())}")

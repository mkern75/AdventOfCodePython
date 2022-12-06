from utils import load_lines
from Device import Device

INPUT_FILE = "./year2018/data/day21.txt"
program = load_lines(INPUT_FILE)

device = Device(program, False)

# part 1: we need to reach instruction #28 and r0==r5 for the program to stop (for my input)
while device.ip != 28:
    device.run_one_cycle()
device.run_one_cycle()
print(f"part 1: {device.reg[5]}")


# part 2: let's code the device logic in python
# idea: what's the longest run that would terminate before the main loop revisits an earlier state
def run():
    res = -1
    cache = set()
    r1 = 0
    r3 = 65_536
    r5 = 733_884
    while True:
        if (r1, r3, r5) in cache:
            return res
        else:
            cache |= {(r1, r3, r5)}
        r1 = r3 & 255
        r5 = (((r5 + r1) & 16_777_215) * 65_899) & 16_777_215
        if r3 < 256:
            res = r5  # here would be the check r5==r0 
            r3 = r5 | 65_536
            r5 = 733_884
        else:
            r3 = r3 // 256


print(f"part 2: {run()}")

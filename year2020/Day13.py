INPUT_FILE = "./year2020/data/day13.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

earliest = int(data[0])
buses = [int(b) for b in data[1].split(",") if b != "x"]
offsets = [t for t, b in enumerate(data[1].split(",")) if b != "x"]

bus = min((earliest, b) if earliest % b == 0 else (earliest - earliest % b + b, b) for b in buses)
ans1 = bus[1] * (bus[0] - earliest)
print(f"part 1: {ans1}")


t, m = 0, 1
for bus, offset in zip(buses, offsets):
    while t % bus != ((bus - offset) % bus + bus) % bus:
        t += m
    m *= bus
print(f"part 2: {t}")

file = open("./year2019/data/day06.txt", "r")
lines = [line.rstrip('\n') for line in file]


def n_direc_orbits(orbit):
    return len(orbit)


def seq_to_com(x, orbit):
    return ["COM"] if x not in orbit else [x] + seq_to_com(orbit[x], orbit)


def n_indirect_orbits(orbit):
    return sum([len(seq_to_com(orbit[x], orbit)) - 1 for x in orbit])


orbit = {}
for line in lines:
    aaa, bbb = line.split(")")
    orbit[bbb] = aaa

ans1 = n_direc_orbits(orbit) + n_indirect_orbits(orbit)
print("part 1:", ans1)

seq_you = seq_to_com(orbit["YOU"], orbit)
seq_santa = seq_to_com(orbit["SAN"], orbit)
ans2 = -1
for x in seq_you:
    if x in seq_santa:
        ans2 = seq_you.index(x) + seq_santa.index(x)
        break
print("part 2:", ans2)

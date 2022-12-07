INPUT_FILE = "./year2022/data/day07.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

root = curr = ("/",)  # folder = tuple of levels from root down to the folder name itself
fs = {root: [[], [], -1]}  # fs = map: folder -> [sub-folders, files, total_size]
for line in data:
    if line == "$ cd /":
        curr = root
    elif line == "$ cd .." and len(curr) > 1:
        curr = curr[:-1]
    elif line.startswith("$ cd"):
        curr += (line[5:],)
    elif line.startswith("$"):
        pass
    elif line.startswith("dir"):
        folder = curr + (line[4:],)
        fs[folder] = [[], [], -1]
        fs[curr][0] += [folder]
    else:
        sz, file = line.split()
        fs[curr][1] += [(file, int(sz))]


def size(d):
    if fs[d][2] == -1:
        fs[d][2] = sum(s for (_, s) in fs[d][1]) + sum(size(c) for c in fs[d][0])
    return fs[d][2]


print(f"part 1: {sum(size(d) for d in fs if size(d) <= 100_000)}")
print(f"part 2: {min(size(d) for d in fs if size(root) - size(d) + 30_000_000 <= 70_000_000)}")

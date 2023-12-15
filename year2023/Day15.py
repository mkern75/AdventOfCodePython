INPUT_FILE = "./year2023/data/day15.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
data = data[0].split(",")


def aoc_hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h


ans1 = sum(map(aoc_hash, data))

boxes = [[] for _ in range(256)]
for step in data:
    i = next(j for j, c in enumerate(step) if c in "=-")
    label = step[:i]
    box_number = aoc_hash(label)
    op = step[i]
    lens = int(step[(i + 1):]) if op == "=" else 0

    if op == "=":
        for i in range(len(boxes[box_number])):
            if boxes[box_number][i][0] == label:
                boxes[box_number][i][1] = lens
                break
        else:
            boxes[box_number] += [[label, lens]]

    elif op == "-":
        for i in range(len(boxes[box_number])):
            if boxes[box_number][i][0] == label:
                boxes[box_number].pop(i)
                break

ans2 = 0
for box_number in range(256):
    for slot, (_, focal_length) in enumerate(boxes[box_number], 1):
        ans2 += (box_number + 1) * slot * focal_length

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

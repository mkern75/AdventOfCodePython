INPUT_FILE = "./year2023/data/day15.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]
data = data[0].split(",")


def aoc_hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h


ans1 = sum(map(aoc_hash, data))

boxes = [{} for _ in range(256)]
for step in data:
    if "=" in step:
        label, lens = step.split("=")
        idx, lens = aoc_hash(label), int(lens)
        boxes[idx][label] = lens
    elif "-" in step:
        label = step[:-1]
        idx = aoc_hash(label)
        if label in boxes[idx]:
            boxes[idx].pop(label)

ans2 = 0
for box_number in range(256):
    for slot, focal_length in enumerate(boxes[box_number].values(), 1):
        ans2 += (box_number + 1) * slot * focal_length

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

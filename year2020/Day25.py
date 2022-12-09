INPUT_FILE = "./year2020/data/day25.txt"
public_key = [int(line.rstrip('\n')) for line in open(INPUT_FILE, "r")]


def crack_loop_size(subject_number, public_key):
    n, loop_size = 1, 0
    while n != public_key:
        n = (n * subject_number) % 20201227
        loop_size += 1
    return loop_size


def transform(subject_number, loop_size):
    n = 1
    for _ in range(loop_size):
        n = (n * subject_number) % 20201227
    return n


loop_size = [crack_loop_size(7, pk) for pk in public_key]
encryption_key = [transform(public_key[i], loop_size[1 - i]) for i in range(2)]
print(f"part 1: {encryption_key[0]}")

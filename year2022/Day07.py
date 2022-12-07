from collections import namedtuple

directory = namedtuple("dir", "name parent_dir child_dirs files")
file = namedtuple("file", "name size")

INPUT_FILE = "./year2022/data/day07.txt"
terminal_output = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def parse(terminal_output):
    root = directory("/", None, {}, {})
    current_dir = root
    for line in terminal_output:
        if line.startswith("$ "):
            command = line[2:]
            if command == "cd /":
                current_dir = root
            elif command == "cd ..":
                if current_dir.parent_dir is not None:
                    current_dir = current_dir.parent_dir
            elif command.startswith("cd "):
                child_dir_name = command[3:]
                if child_dir_name not in current_dir.child_dirs:
                    child_dir = directory(child_dir_name, current_dir, {}, {})
                    current_dir.child_dirs[child_dir_name] = child_dir
                current_dir = current_dir.child_dirs[child_dir_name]
            else:
                pass
        else:
            if line.startswith("dir "):
                child_dir_name = line[4:]
                if child_dir_name not in current_dir.child_dirs:
                    child_dir = directory(child_dir_name, current_dir, {}, {})
                    current_dir.child_dirs[child_dir_name] = child_dir
            else:
                size, file = line.split()
                if file not in current_dir.files:
                    current_dir.files[file] = int(size)
    return root


# to be improved to avoid recomputation
def total_size(d):
    return sum(s for s in d.files.values()) + sum(total_size(c) for c in d.child_dirs.values())


def part_1(d):
    return (total_size(d) if total_size(d) <= 100_000 else 0) + sum(part_1(c) for c in d.child_dirs.values())


def part_2(d):
    to_free = 30_000_000 - 70_000_000 + total_size(d)
    if to_free <= 0:
        return None
    smallest = total_size(d)
    queue = [d]
    while queue:
        x = queue.pop()
        if to_free <= total_size(x) < smallest:
            smallest = total_size(x)
        queue.extend(x.child_dirs.values())
    return smallest


root = parse(terminal_output)
print(f"part 1: {part_1(root)}")
print(f"part 2: {part_2(root)}")

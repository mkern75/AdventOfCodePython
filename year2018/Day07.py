from utils import load_lines
from collections import defaultdict

INPUT_FILE = "./year2018/data/day07.txt"


def topological_sort(nodes, edges):
    incoming_edges = defaultdict(set)
    for (fr, to) in edges:
        incoming_edges[to].add(fr)

    tsort, avail = [], []
    for n in nodes:
        if len(incoming_edges[n]) == 0:
            avail += [n]

    while len(avail) > 0:
        avail.sort()
        node = avail.pop(0)
        tsort += [node]
        for n, p in incoming_edges.items():
            if node in p:
                p.discard(node)
                if len(p) == 0:
                    avail += [n]

    return tsort


def topological_sort_part2(nodes, edges, step, n_parallel):
    incoming_edges = defaultdict(set)
    for (fr, to) in edges:
        incoming_edges[to].add(fr)

    tsort, avail, in_process = [], [], []
    for n in nodes:
        if len(incoming_edges[n]) == 0:
            avail += [n]

    t_current = 0

    while len(avail) > 0 or len(in_process) > 0:

        avail.sort()
        while len(avail) > 0 and len(in_process) < n_parallel:
            node = avail.pop(0)
            t_finish = t_current + step + (ord(node) - ord("A") + 1)
            in_process += [(t_finish, node)]

        t_current = min([t_finish for (t_finish, _) in in_process])
        for i in range(len(in_process) - 1, -1, -1):
            if in_process[i][0] == t_current:
                node = in_process.pop(i)[1]
                tsort += [node]
                for n, p in incoming_edges.items():
                    if node in p:
                        p.discard(node)
                        if len(p) == 0:
                            avail += [n]

    return tsort, t_current


nodes = set()
edges = set()
for line in load_lines(INPUT_FILE):
    s = line.split()
    nodes.update([s[1], s[7]])
    edges.add((s[1], s[7]))

ans1 = "".join(list(topological_sort(nodes, edges)))
print("part 1:", ans1)

_, ans2 = topological_sort_part2(nodes, edges, 60, 5)
print("part 2:", ans2)

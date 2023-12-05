INPUT_FILE = "./year2023/data/day05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

# read seed numbers from first line
seeds = list(map(int, data[0].split(":")[1].split()))

# read mappings block by block and save as tuples
mappings = []
for line in data[2:]:
    if "map:" in line:
        mappings += [[]]
    elif line:
        mappings[-1] += [tuple(map(int, line.split()))]

for part in [1, 2]:
    if part == 1:
        rng = [(x, x + 1) for x in seeds]  # current ranges is list of pairs [start, end)
    else:
        rng = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for mapping in mappings:
        rng_new = []
        while rng:
            rng_start, rng_end = rng.pop()
            for dst_start, src_start, src_len in mapping:
                overlap_start = max(rng_start, src_start)
                overlap_end = min(rng_end, src_start + src_len)
                if overlap_start < overlap_end:  # overlap found
                    rng_new += [(dst_start + (overlap_start - src_start), dst_start + (overlap_end - src_start))]
                    if rng_start < overlap_start:
                        rng += [(rng_start, overlap_start)]
                    if overlap_end < rng_end:
                        rng += [(overlap_end, rng_end)]
                    break
            else:
                rng_new += [(rng_start, rng_end)]  # no mapping found, thus range remains the same
        rng = rng_new

    ans = min(start for start, _ in rng)
    print(f"part {part}: {ans}")

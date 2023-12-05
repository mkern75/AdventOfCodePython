INPUT_FILE = "./year2023/data/day05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

# read seed numbers from first line
seeds = list(map(int, data[0].split(":")[1].split()))

# read mappings block by block and save as tuples (src_from, src_to, dst_from, dst_to) (inclusive)
mappings = []
for line in data[2:]:
    if ":" in line:
        mappings += [[]]
    elif line:
        dst_from, src_from, rng_len = map(int, line.split())
        mappings[-1] += [(src_from, src_from + rng_len - 1, dst_from, dst_from + rng_len - 1)]

for part in [1, 2]:
    # build seed ranges depending on part 1 or 2
    if part == 1:
        rng = [(x, x) for x in seeds]
    else:
        rng = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    # apply all mappings
    for mapping in mappings:
        rng_new = []
        while rng:
            rng_frm, rng_to = rng.pop()
            for src_frm, src_to, dst_frm, dst_to in mapping:
                # overlap found
                if rng_frm <= src_to and src_frm <= rng_to:
                    start, end = max(rng_frm, src_frm), min(rng_to, src_to)
                    start_offset, end_offset = start - src_frm, end - src_frm
                    rng_new += [(dst_frm + start_offset, dst_frm + end_offset)]
                    # remaining unmapped parts of the range
                    if rng_frm < start:
                        rng += [(rng_frm, start - 1)]
                    if end < rng_to:
                        rng += [(end + 1, rng_to)]
                    break
            else:
                # no mapping found, thus range stays the same
                rng_new += [(rng_frm, rng_to)]
        rng = rng_new

    # calculate answer
    ans = min(a for a, _ in rng)
    print(f"part {part}: {ans}")

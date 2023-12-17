from collections import defaultdict
import heapq

INPUT_FILE = "./year2023/data/day17.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

grid = [[int(c) for c in line] for line in data]
R, C = len(grid), len(grid[0])


def explore(min_steps_same_dir, max_steps_same_dir):
    min_heat_loss = defaultdict(lambda: 10 ** 20)
    # format: (heat_loss_so_far, row, column, direction_delta_row, direction_delta_column, steps_in_current_direction)
    heap = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
    heapq.heapify(heap)

    while heap:
        heat_loss, r, c, dr, dc, steps = heapq.heappop(heap)

        # destination reached
        if (r, c) == (R - 1, C - 1) and steps >= min_steps_same_dir:
            return heat_loss

        if heat_loss >= min_heat_loss[r, c, dr, dc, steps]:
            continue
        min_heat_loss[r, c, dr, dc, steps] = heat_loss

        for ndr, ndc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + ndr
            nc = c + ndc
            nsteps = steps + 1 if (ndr, ndc) == (dr, dc) else 1

            # must stay within the grid
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            # no turning back
            if (ndr, ndc) == (-dr, -dc):
                continue
            # same direction for too long
            if (ndr, ndc) == (dr, dc) and steps == max_steps_same_dir:
                continue
            # turn too early
            if (ndr, ndc) != (dr, dc) and steps < min_steps_same_dir:
                continue

            nheat_loss = heat_loss + grid[nr][nc]
            if nheat_loss < min_heat_loss[nr, nc, ndr, ndc, nsteps]:
                heapq.heappush(heap, (nheat_loss, nr, nc, ndr, ndc, nsteps))


ans1 = explore(0, 3)
print(f"part 1: {ans1}")
ans2 = explore(4, 10)
print(f"part 2: {ans2}")

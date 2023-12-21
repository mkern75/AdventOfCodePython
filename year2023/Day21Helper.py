from collections import Counter

INPUT_FILE = "./year2023/data/day21.txt"
grid = [list(line.rstrip("\n")) for line in open(INPUT_FILE, "r")]
R, C = len(grid), len(grid[0])
steps = 26501365

# some key assertions
assert R == C
assert R & 1
assert grid[R // 2][C // 2] == "S"
assert all(grid[r][C // 2] for r in range(R))
assert all(grid[R // 2][c] for c in range(C))
assert steps % R == R // 2


def simulate(n_steps, r_start, c_start):
    loc = {(r_start, c_start)}
    n_loc = [len(loc)]
    for cycle in range(n_steps):
        loc_new = set()
        for r, c in loc:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rn, cn = r + dr, c + dc
                if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                    loc_new |= {(rn, cn)}
        loc = loc_new
        n_loc += [len(loc)]
    return n_loc


def simulate_infinity(n_steps, r_start, c_start):
    loc = {(r_start, c_start)}
    for cycle in range(n_steps):
        loc_next = set()
        for r, c in loc:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rn, cn = r + dr, c + dc
                if grid[rn % R][cn % C] != "#":
                    loc_next |= {(rn, cn)}
        loc = loc_next
    return loc


r_start, c_start = R // 2, C // 2

for factor in range(1, 10):

    steps_test = factor * R + R // 2
    loc = simulate_infinity(steps_test, r_start, c_start)

    # the following counter can be used to look at indiviudal grid "copies" to make sure we
    # consider all the different pieces together (I did that for factors 2 and 3)
    cnt = Counter([(r // R, c // C) for r, c in loc])

    n_even = simulate(3 * R + 1, r_start, c_start)[-1]
    n_odd = simulate(3 * R, r_start, c_start)[-1]
    from_north = simulate(R, 0, c_start)
    from_south = simulate(R, R - 1, c_start)
    from_west = simulate(R, r_start, 0)
    from_east = simulate(R, r_start, C - 1)
    from_northwest = simulate(2 * R, 0, 0)
    from_northeast = simulate(2 * R, 0, C - 1)
    from_southwest = simulate(2 * R, R - 1, 0)
    from_southeast = simulate(2 * R, R - 1, C - 1)

    sim_ans = sum(cnt.values())

    calc_ans = 0
    calc_ans += from_southeast[R // 2 - 1] + from_south[R - 1] + from_southwest[R // 2 - 1]
    calc_ans += from_northeast[R // 2 - 1] + from_north[R - 1] + from_northwest[R // 2 - 1]
    calc_ans += from_east[R - 1] + from_west[R - 1]
    calc_ans += n_odd if steps_test & 1 else n_even
    calc_ans += 2 * ((factor - 1) // 2) * (n_odd if steps_test & 1 else n_even)
    calc_ans += 2 * (factor // 2) * (n_odd if steps_test & 1 == 0 else n_even)
    for i in range(1, factor):
        calc_ans += from_southeast[R + R // 2 - 1] + from_southeast[R // 2 - 1]
        calc_ans += from_southwest[R + R // 2 - 1] + from_southwest[R // 2 - 1]
        calc_ans += from_northeast[R + R // 2 - 1] + from_northeast[R // 2 - 1]
        calc_ans += from_northwest[R + R // 2 - 1] + from_northwest[R // 2 - 1]
        c1 = 2 * ((factor - i - 1) // 2)
        c2 = 2 * ((factor - i) // 2)
        if i & 1:
            calc_ans += 2 * (n_odd if steps_test & 1 == 0 else n_even)
            calc_ans += 2 * c1 * (n_odd if steps_test & 1 == 0 else n_even)
            calc_ans += 2 * c2 * (n_odd if steps_test & 1 == 1 else n_even)
        else:
            calc_ans += 2 * (n_odd if steps_test & 1 == 1 else n_even)
            calc_ans += 2 * c1 * (n_odd if steps_test & 1 == 1 else n_even)
            calc_ans += 2 * c2 * (n_odd if steps_test & 1 == 0 else n_even)

    if sim_ans == calc_ans:
        print(f"Success for factor {factor}: simulated and calculated answers match; {calc_ans}.")
    else:
        print(f"Issue for factor {factor}: simulated and calculated answers do not match; {sim_ans} vs {calc_ans}.")

    assert sim_ans == calc_ans

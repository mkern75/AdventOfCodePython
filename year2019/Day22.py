import re

INPUT_FILE = "./year2019/data/day22.txt"
shuffle_process = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def get_shuffle_coefficients(shuffle_process, n_cards, repeats=1):
    """Represent (overall) shuffle as 'y=a*x+b MOD n_cards' where x is the initial and y the final position"""
    a, b = 1, 0
    for shuffle in shuffle_process:
        if shuffle == "deal into new stack":
            a = (-a) % n_cards
            b = ((n_cards - 1) - b) % n_cards
        elif x := re.search(r"deal with increment (.*)", shuffle):
            inc = int(x.groups()[0])
            a = (a * inc) % n_cards
            b = (b * inc) % n_cards
        elif x := re.search(r"cut (.*)", shuffle):
            cut = int(x.groups()[0])
            a = a % n_cards
            b = (b - cut) % n_cards
    if repeats > 1:  # adjust for repetitions of shuffle process
        if a == 1:
            a, b = a, (b * repeats) % n_cards
        else:
            a, b = pow(a, repeats, n_cards), (b * (pow(a, repeats, n_cards) - 1) * pow(a - 1, -1, n_cards)) % n_cards
    return a, b


# part 1
N = 10_007
a, b = get_shuffle_coefficients(shuffle_process, N)
ans1 = (a * 2019 + b) % N
print(f"part 1: {ans1}")

# part 2
N = 119_315_717_514_047
repeats = 101_741_582_076_661
a, b = get_shuffle_coefficients(shuffle_process, N, repeats)
ans2 = ((2020 - b) * pow(a, -1, N)) % N  # ax+b = 2020 MOD N  =>  x = (2020-b) / a  MOD N
print(f"part 2: {ans2}")

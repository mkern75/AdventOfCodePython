import math
from itertools import combinations

file = open("./year2015/data/day24.txt", "r")
lines = [line.rstrip('\n') for line in file]


def sub(alist, alist_to_sub):
    return [e for e in alist if e not in alist_to_sub]


def select_n_weights(n, weights, target_weight):
    return [c for c in combinations(weights, n) if sum(c) == target_weight]


def n_split_possible(n, weights, target_weight):
    for i in range(1, len(weights) // n + 1):
        for c in combinations(weights, i):
            if sum(c) == target_weight:
                if n == 2 or n_split_possible(n - 1, sub(weights, c), target_weight):
                    return True
    return False


def find_best_split(weights, n):
    best = math.inf
    target_weight = sum(weights) // n
    if target_weight * n != sum(weights):
        return math.inf
    for i in range(1, len(weights) // n + 1):
        for c in select_n_weights(i, weights, target_weight):
            remaining_weights = sub(weights, c)
            if n_split_possible(n - 1, remaining_weights, target_weight):
                best = min(best, math.prod(c))
        if best != math.inf:
            return best
    return math.inf


weights = [int(line) for line in lines]
print(find_best_split(weights, 3))
print(find_best_split(weights, 4))

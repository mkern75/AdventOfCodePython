from collections import Counter

INPUT_FILE = "./year2023/data/day07.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

CARD_SET_1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_SET_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def card_value(card, card_set):
    return card_set.index(card)


def hand_type_value(hand, card_set, replace_joker):
    if not replace_joker:
        return hand_type_helper(hand, card_set)
    else:
        return max(hand_type_helper(hand.replace("J", card), card_set) for card in card_set)


def hand_type_helper(hand, card_set):
    freq = [0] * len(card_set)
    for card in hand:
        freq[card_set.index(card)] += 1
    cnt = Counter(freq)
    if cnt[5] == 1:
        return 6
    elif cnt[4] == 1:
        return 5
    elif cnt[3] == 1 and cnt[2] == 1:
        return 4
    elif cnt[3] == 1:
        return 3
    elif cnt[2] == 2:
        return 2
    elif cnt[2] == 1:
        return 1
    else:
        return 0


def hand_value(hand, card_set, replace_joker=False):
    return (hand_type_value(hand, card_set, replace_joker),) + tuple(card_value(card, card_set) for card in hand)


hands = []
for line in data:
    hand, bid = line.split()
    hands += [(hand, int(bid))]

hands.sort(key=lambda hand: hand_value(hand[0], CARD_SET_1, False))
ans1 = sum(rank * hand[1] for rank, hand in enumerate(hands, 1))

hands.sort(key=lambda hand: hand_value(hand[0], CARD_SET_2, True))
ans2 = sum(rank * hand[1] for rank, hand in enumerate(hands, 1))

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

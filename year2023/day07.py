from collections import Counter

INPUT_FILE = "./year2023/data/day07.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

DECK_1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
DECK_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def card_value(card, deck):
    return deck.index(card)


def hand_type_value(hand, deck, replace_joker=False):
    return max(score(hand.replace("J", card)) for card in deck) if replace_joker else score(hand)


def score(hand):
    cnt = Counter(Counter(hand).values())
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


def hand_value(hand, deck, replace_joker=False):
    return (hand_type_value(hand, deck, replace_joker),) + tuple(card_value(card, deck) for card in hand)


hands = []
for line in data:
    hand, bid = line.split()
    hands += [(hand, int(bid))]

hands.sort(key=lambda hand: hand_value(hand[0], DECK_1, False))
ans1 = sum(rank * hand[1] for rank, hand in enumerate(hands, 1))

hands.sort(key=lambda hand: hand_value(hand[0], DECK_2, True))
ans2 = sum(rank * hand[1] for rank, hand in enumerate(hands, 1))

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

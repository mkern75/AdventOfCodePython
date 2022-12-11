from collections import deque

INPUT_FILE = "./year2020/data/day22.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


class Game1:
    def __init__(self, deck1, deck2):
        self.deck1 = deque(deck1)
        self.deck2 = deque(deck2)
        self.winner = None

    def play(self):
        while self.deck1 and self.deck2:
            card1 = self.deck1.popleft()
            card2 = self.deck2.popleft()
            if card1 > card2:
                self.deck1.append(card1)
                self.deck1.append(card2)
            else:
                self.deck2.append(card2)
                self.deck2.append(card1)
        self.winner = 1 if self.deck1 else 2

    def score(self):
        deck = self.deck1 if self.winner == 1 else self.deck2
        return sum(i * deck[len(deck) - i] for i in range(1, len(deck) + 1))


class Game2:
    def __init__(self, deck1, deck2, debug=False):
        self.deck1 = deque(deck1)
        self.deck2 = deque(deck2)
        self.hist = set()
        self.debug = debug
        self.winner = None

    def play(self):
        while self.deck1 and self.deck2:
            state = (tuple(self.deck1), tuple(self.deck2))
            if state in self.hist:
                self.winner = 1
                return
            self.hist.add(state)
            card1 = self.deck1.popleft()
            card2 = self.deck2.popleft()
            if len(self.deck1) < card1 or len(self.deck2) < card2:
                if card1 > card2:
                    self.deck1.append(card1)
                    self.deck1.append(card2)
                else:
                    self.deck2.append(card2)
                    self.deck2.append(card1)
            else:
                sub_game = Game2(list(self.deck1)[:card1], list(self.deck2)[:card2], self.debug)
                sub_game.play()
                if sub_game.winner == 1:
                    self.deck1.append(card1)
                    self.deck1.append(card2)
                else:
                    self.deck2.append(card2)
                    self.deck2.append(card1)
        self.winner = 1 if self.deck1 else 2

    def score(self):
        deck = self.deck1 if self.winner == 1 else self.deck2
        return sum(i * deck[len(deck) - i] for i in range(1, len(deck) + 1))


# parse data
deck, p = [[], []], 0
for line in data:
    if line.isnumeric():
        deck[p] += [int(line)]
    elif line == "Player 2:":
        p += 1

# part 1
game1 = Game1(deck[0], deck[1])
game1.play()
print(f"part 1: {game1.score()}")

# part 2
game2 = Game2(deck[0], deck[1])
game2.play()
print(f"part 1: {game2.score()}")

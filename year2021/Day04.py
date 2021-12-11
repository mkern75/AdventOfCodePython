import numpy as np

file = open("./data/year2021/day04.txt", "r")
lines = [line.rstrip('\n').split() for line in file]

numbers = [int(x) for x in lines[0][0].split(",")]
N = (len(lines) - 1) // 6
bingo = np.zeros(N, dtype=bool)
boards = np.zeros((N, 5, 5), dtype=int)
for i in range(N):
    for r in range(5):
        boards[i][r] = [int(x) for x in lines[2 + i * 6 + r]]


def is_bingo(board):
    for i in range(5):
        br, bc = True, True
        for j in range(5):
            br = br and (board[i][j] < 0)
            bc = bc and (board[j][i] < 0)
        if br or bc:
            return True
    return False


for number in numbers:
    for i in range(N):
        if not bingo[i]:
            boards[i][boards[i] == number] = -1
            if is_bingo(boards[i]):
                bingo[i] = True
                if np.count_nonzero(bingo) in [1, N]:
                    print(number * np.sum(boards[i][boards[i] >= 0]))
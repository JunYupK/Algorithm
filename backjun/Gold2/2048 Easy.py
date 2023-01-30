import sys
from itertools import product

input = sys.stdin.readline
# index = 0
# while index < 5 - 1:
#     print(index)
#     index += 1
N = int(input())
board, check = [], []
moves = ["UP", "DOWN", "LEFT", "RIGHT"]
for _ in range(N):
    board.append(list(map(int, input().split())))


def simulation(move):
    if move == "UP":
        # 위로 밀기
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if board[i][j] == 0:
                    next_x = i
                    while next_x != N - 1:
                        tmp = board[next_x + 1][j]
                        board[next_x + 1][j] = board[next_x][j]
                        board[next_x][j] = tmp
                        next_x += 1
        # 합치기
        for j in range(N):
            index = 0
            while index < N - 1:
                if board[index][j] == board[index + 1][j]:
                    board[index][j] += board[index + 1][j]
                    board[index + 1][j] = 0
                    index += 2
                else:
                    index += 1
        # 합친 후 다시 밀기
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if board[i][j] == 0:
                    next_x = i
                    while next_x != N - 1:
                        tmp = board[next_x + 1][j]
                        board[next_x + 1][j] = board[next_x][j]
                        board[next_x][j] = tmp
                        next_x += 1
    elif move == "DOWN":
        # 아래로 밀기
        for j in range(N):
            for i in range(N):
                if board[i][j] == 0:
                    next_x = i
                    while next_x != 0:
                        tmp = board[next_x - 1][j]
                        board[next_x - 1][j] = board[next_x][j]
                        board[next_x][j] = tmp
                        next_x -= 1
        # 아래로 합치기
        for j in range(N):
            index = N - 1
            while index >= 0:
                if board[index][j] == board[index - 1][j]:
                    board[index][j] += board[index - 1][j]
                    board[index - 1][j] = 0
                    index -= 2
                else:
                    index -= 1
        # 아래로 밀기
        for j in range(N):
            for i in range(N):
                if board[i][j] == 0:
                    next_x = i
                    while next_x != 0:
                        tmp = board[next_x - 1][j]
                        board[next_x - 1][j] = board[next_x][j]
                        board[next_x][j] = tmp
                        next_x -= 1
    elif move == "LEFT":
        # 왼쪽으로 밀기
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[i][j] == 0:
                    next_y = j
                    while next_y != N - 1:
                        board[i][next_y] = board[i][next_y + 1]
                        board[i][next_y + 1] = 0
                        next_y += 1
        # 합치기
        for i in range(N):
            index = 0
            while index < N - 1:
                if board[i][index] == board[i][index + 1]:
                    board[i][index] += board[i][index + 1]
                    board[i][index + 1] = 0
                    index += 2
                else:
                    index += 1
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[i][j] == 0:
                    next_y = j
                    while next_y != N - 1:
                        board[i][next_y] = board[i][next_y + 1]
                        board[i][next_y + 1] = 0
                        next_y += 1

    elif move == "RIGHT":
        # 오른쪽으로 밀기
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    next_y = j
                    while next_y != 0:
                        board[i][next_y] = board[i][next_y - 1]
                        board[i][next_y - 1] = 0
                        next_y -= 1
        for j in range(N):
            index = N - 1
            while index >= 0:
                if board[j][index] == board[j][index - 1]:
                    board[j][index] += board[j][index - 1]
                    board[j][index - 1] = 0
                    index -= 2
                else:
                    index -= 1
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    next_y = j
                    while next_y != 0:
                        board[i][next_y] = board[i][next_y - 1]
                        board[i][next_y - 1] = 0
                        next_y -= 1


for move in product(moves, repeat=5):
    for m in move:
        simulation(m)
    for i in range(N):
        print(board[i])
    print()

import sys
from itertools import product

input = sys.stdin.readline
N = int(input())
pure_board, check = [], []
moves = ["UP", "DOWN", "LEFT", "RIGHT"]
for _ in range(N):
    pure_board.append(list(map(int, input().split())))

def simulation(moves_list, board):
    for move in moves_list:
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
                while index > 0:
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
                while index > 0:
                    if board[j][index] == board[j][index - 1]:
                        board[j][index] *= 2
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
    return board

_max = 0
for move in product(moves, repeat=5):
    check = [pure_board[i][:] for i in range(N)]
    simulation(move,check)
    for i in range(N):
        for j in range(N):
            if _max < check[i][j]:
                _max = check[i][j]
print(_max)

# simulation(["UP"], pure_board)
# print("***************************************")
# for i in range(N):
#     print(pure_board[i])
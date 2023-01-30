import sys
import heapq

input = sys.stdin.readline
R, C, M = map(int, input().split())
current_board = [[0] * (C + 1) for _ in range(R + 1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    current_board[r][c] = (s, d, z)


def move_shark(board):
    new_board = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if board[i][j]:
                speed, dir, size = board[i][j]
                next_i, next_j = i, j
                moveCount = speed
                while moveCount != 0:
                    if dir == 1:
                        if next_i == 1:
                            dir = 2
                            next_i += 1
                        else:
                            next_i -= 1
                    elif dir == 2:
                        if next_i == R:
                            dir = 1
                            next_i -= 1
                        else:
                            next_i += 1
                    elif dir == 3:
                        if next_j == C:
                            dir = 4
                            next_j -= 1
                        else:
                            next_j += 1
                    elif dir == 4:
                        if next_j == 1:
                            dir = 3
                            next_j += 1
                        else:
                            next_j -= 1
                    moveCount -= 1
                if new_board[next_i][next_j] != 0 and new_board[next_i][next_j][2] <= size:
                    new_board[next_i][next_j] = (speed, dir, size)
                elif new_board[next_i][next_j] == 0:
                    new_board[next_i][next_j] = (speed, dir, size)
    return new_board


answer = 0
for i in range(1, C + 1):
    for j in range(1, R + 1):
        if current_board[j][i]:
            answer += current_board[j][i][2]
            current_board[j][i] = 0
            break
    current_board = move_shark(current_board)

print(answer)

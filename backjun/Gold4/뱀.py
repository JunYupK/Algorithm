import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
direct = [(0,1), (1,0), (0,-1), (-1, 0)]
snake = [[0,0], [0,0], 0]
q = deque()
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j = map(int,input().split())
    board[i-1][j-1] = 1
L = int(input())
for _ in range(L):
    tmp = list(input().split())
    q.append((int(tmp[0]), tmp[1]))
board[0][0] = 2
time = 0
snake_body = deque()
snake_body.append((0,0))
while True:
    if q:
        check, flag = q.popleft()
    pos_x, pos_y = snake[0]
    next_x, next_y = pos_x + direct[snake[2]][0], pos_y + direct[snake[2]][1]
    time += 1
    if check == time:
        if flag == 'L':
            if snake[2] == 0:
                snake[2] = 3
            else:
                snake[2] -= 1
        else:
            snake[2] = (snake[2] + 1) % 4
    else:
        q.appendleft((check,flag))
    if 0 <= next_x < N and 0 <= next_y < N:
        if board[next_x][next_y] == 0:
            snake[0] = [next_x, next_y]
            board[next_x][next_y] = 2
            tail_x, tail_y = snake_body.popleft()
            board[tail_x][tail_y] = 0
            snake_body.append((next_x,next_y))
        elif board[next_x][next_y] == 1:
            snake[0] = [next_x, next_y]
            board[next_x][next_y] = 2
            snake_body.append((next_x,next_y))
        elif board[next_x][next_y] == 2:
            break
    else:
        break


print(time)

#1차 접근 아이디어 => 외부공기와 내부 공기를 구분해보자 외부공기 0 내부공기 3
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
moves = [[-1,0], [1,0], [0,-1], [0,1]]
def outAir():
    q = deque()
    visited = [[False] * M for _ in range(N)]
    q.append((0,0))
    visited[0][0] = True
    board[0][0] = 3
    isCheeze = False
    while q:
        x, y = q.popleft()
        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if 0 <= dx < N and 0 <= dy < M:
                if board[dx][dy] != 1 and visited[dx][dy] is False:
                    visited[dx][dy] = True
                    board[dx][dy] = 3
                    q.append((dx, dy))
                if board[dx][dy] == 1:
                    isCheeze = True
    return isCheeze

def checkCheeze():
    q = deque()
    visited = [[False] * M for _ in range(N)]
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if 0 <= dx < N and 0 <= dy < M:
                if board[dx][dy] != 1 and visited[dx][dy] is False:
                    visited[dx][dy] = True
                    board[dx][dy] = 3
                    q.append((dx, dy))
                if board[dx][dy] == 1 and visited[dx][dy] is False:
                    visited[dx][dy] = True
                    count = 0
                    for check in moves:
                        tmp_x, tmp_y = dx + check[0], dy + check[1]
                        if board[tmp_x][tmp_y] == 3:
                            count += 1
                        if count >= 2:
                            board[dx][dy] = 5

flag = True
outAir()
time = 0
while flag:
    checkCheeze()
    flag = outAir()
    time += 1
print(time)
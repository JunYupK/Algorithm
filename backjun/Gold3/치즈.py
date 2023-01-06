#1차 접근 아이디어 => 외부공기와 내부 공기를 구분해보자 외부공기 0 내부공기 3
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
moves = [[-1,0], [1,0], [0,-1], [0,1]]
def bfs():
    q = deque()
    isCheeze = False
    start = board[0][0]
    q.append((0,0))
    board[0][0] = 3
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for move in moves:
            dx, dy = x+move[0], y+move[1]
            if 0<=dx<N and 0<=dy<M:
                if visited[dx][dy] is False and board[dx][dy] == start:
                    q.append((dx,dy))
                    visited[dx][dy] = True
                    board[dx][dy] = 3
                if board[dx][dy] == 1:
                    board[dx][dy] = 3
                    isCheeze = True
    return isCheeze

flag = True
time = 1
while flag:
    flag = bfs()
    time += 1
print(time)
import sys
from collections import deque

N, M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input())))
moves = [(-1,0), (1,0), (0,-1), (0,1)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, flag = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][flag]
        for move in moves:
            dx, dy = x+move[0], y+move[1]
            if 0 <= dx < N and 0 <= dy < M:
                if visited[dx][dy][flag] == 0 and board[dx][dy] == 0:
                    q.append((dx,dy,flag))
                    visited[dx][dy][flag] = visited[x][y][flag] + 1
                if visited[dx][dy][flag] == 0 and board[dx][dy] == 1 and flag == 0:
                    q.append((dx,dy, 1))
                    visited[dx][dy][1] = visited[x][y][flag] + 1
    return -1
print(bfs())

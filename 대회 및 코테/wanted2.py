import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(N):
    board.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
answer = 0


def bfs(i, j):
    q = deque()
    q.append((i, j))
    board[i][j] = -1
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for move in moves:
            next_x, next_y = x + move[0], y + move[1]
            if next_x == -1:
                next_x = N - 1
            if next_x == N:
                next_x = 0
            if next_y == -1:
                next_y = M - 1
            if next_y == M:
                next_y = 0
            if visited[next_x][next_y] is False and board[next_x][next_y] == 0:
                board[next_x][next_y] = -1
                q.append((next_x, next_y))
                visited[next_x][next_y] = True


for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            bfs(i, j)
            answer += 1

print(answer)

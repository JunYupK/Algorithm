import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
board = []
answer = []
index = []
moves = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == '1':
            index.append((i,j))
    tmp.pop()
    board.append(tmp)
    answer.append(tmp)
def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    count = 1
    while q:
        x, y = q.popleft()
        for move in moves:
            next_x, next_y = x+move[0], y+move[1]
            if 0<=next_x<N and 0<=next_y<M and board[next_x][next_y] == '0' and visited[next_x][next_y] is False:
                visited[next_x][next_y] = True
                q.append((next_x,next_y))
                count += 1
    return count

for i, j in index:
    answer[i][j] = str(bfs(i,j) % 10)

for i in range(N):
    print("".join(answer[i]))


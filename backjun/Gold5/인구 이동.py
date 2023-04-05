import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int,input().split())
moves = [[-1,0],[1,0], [0,1],[0,-1]]
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
day = 0
while 1:
    visited = [[False] * N for _ in range(N)]
    groups = []
    g_count = 0
    for i in range(N):
        for j in range(N):
            for dx, dy in moves:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < N and 0 <= next_y < N:
                    diff = abs(board[i][j] - board[next_x][next_y])
                    if L <= diff <= R:
                        if visited[i][j] is False:
                            g_count += 1
                            visited[i][j] = g_count
                            visited[next_x][next_y] = g_count
                        else:
                            visited[next_x][next_y] = visited[i][j]
    def bfs(x, y, flag):
        result = []
        q = deque()
        q.append((x,y))
        visited[x][y] = False
        result.append((x,y))
        while q:
            pos_x, pos_y = q.popleft()
            for dx, dy in moves:
                next_x, next_y = pos_x + dx , pos_y + dy
                if 0 <= next_x < N and 0 <= next_y < N:
                    if visited[next_x][next_y] == flag:
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = False
                        result.append((next_x, next_y))
        return result
    for i in range(N):
        for j in range(N):
            if visited[i][j] is not False:
                groups.append(bfs(i,j, visited[i][j]))
    if len(groups) == 0:
        break
    for group in groups:
        _sum = 0
        for i, j in group:
            _sum += board[i][j]
        for i, j in group:
            board[i][j] = _sum // len(group)
    day += 1
print(day)


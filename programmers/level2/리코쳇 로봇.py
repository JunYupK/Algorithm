
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
from collections import deque
def solution(board):
    answer = -1
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i,j,0))
                visited[i][j] = True
                break
    while q:
        x,y,count= q.popleft()
        if board[x][y] == 'G':
            return count
        for dx,dy in moves:
            next_x, next_y = x + dx, y + dy
            while 1:
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                        break
                if board[next_x][next_y] == 'D':
                    break
                next_x += dx
                next_y += dy

            next_x -= dx
            next_y -= dy
            if 0 <= next_x < n and 0 <= next_y < m:
                if board[next_x][next_y] != 'D' and visited[next_x][next_y] == False:
                    q.append((next_x, next_y, count+1))
                    visited[next_x][next_y] = True
    return answer
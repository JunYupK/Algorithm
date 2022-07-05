def BFS(board,visited, start):
    x, y = start
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    count = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x > len(board) - 1 or next_y < 0 or next_y > len(board) -1:
                continue
            if board[next_x][next_y] == board[x][y] and visited[next_x][next_y] is False:
                visited[next_x][next_y] = True
                q.append((next_x,next_y))
                count += 1
    return count

from collections import deque
n = int(input())
board = []
color_board = []
for _ in range(n):
    tmp = input()
    board.append(list(tmp))
    tmp = tmp.replace('G','R')
    color_board.append(list(tmp))

visited = [[False] * n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            check = 0
            check = BFS(board,visited,[i,j])
            if check > 0:
                count += 1
print(count, end=" ")


visited = [[False] * n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            check = 0
            check = BFS(color_board,visited,[i,j])
            if check > 0:
                count += 1
print(count, end="")
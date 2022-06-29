from collections import deque
def BFS(board, visited, position):
    x, y = position
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    count = 0
    q.append((x,y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        count += 1
        for k in range(4):
            next_x, next_y = x+dx[k] , y + dy[k]
            if next_x < 0 or next_x > len(board) - 1 or next_y < 0 or next_y > len(board) - 1:
                continue
            if visited[next_x][next_y] is False and board[next_x][next_y] == 1:
                q.append((next_x,next_y))
                visited[next_x][next_y]= True
    return count
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input())))


answer = []
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] is False and board[i][j] == 1:
            answer.append(BFS(board,visited,[i,j]))

answer.sort()
print(len(answer))
for a in answer:
    print(a)



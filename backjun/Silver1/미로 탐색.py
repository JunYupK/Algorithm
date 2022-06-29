from collections import deque
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * M for _ in range(N)]
q = deque()
q.append((0, 0, 1))
visited[0][0] = True
while q:
    x, y, count = q.popleft()
    if x == N-1 and y == M-1:
        print(count)
        break
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if next_x < 0 or next_x > N-1 or next_y < 0 or next_y > M-1:
            continue

        if visited[next_x][next_y] is False and board[next_x][next_y] == 1:
            q.append((next_x, next_y, count + 1))
            visited[next_x][next_y] = True

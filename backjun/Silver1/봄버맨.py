from collections import deque
r,c,n = map(int,input().split())
board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
time = 1
for i in range(r):
    tmp = input()
    tmp = list(tmp)
    board.append(tmp)

while time != n:
    q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                q.append((i,j))
    board = [['O']*c for _ in range(r)]
    time += 1
    if time == n:
        break
    # 폭탄터트리기
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if next_x < 0 or next_x > r-1 or next_y <0 or next_y > c -1:
                continue
            board[next_x][next_y] = '.'
    time += 1
    if time == n:
        break

for d in board:
    print("".join(d))
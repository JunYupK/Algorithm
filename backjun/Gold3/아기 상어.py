from collections import deque
n = int(input())
board = []
result = 0
fish = 0
eat_count = 0
shark_x, shark_y, shark_size = 0,0,2
for i in range(n):
    tmp = list(map(int,input().split()))
    for t in range(len(tmp)):
        if tmp[t] == 9:
            shark_x, shark_y = i, t
        elif 1 <= tmp[t] <= 6:
            fish += 1
    board.append(tmp)
board[shark_x][shark_y] = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def eat_fish(shark_x, shark_y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((shark_x, shark_y))
    visited[shark_x][shark_y] = 1
    temp = []
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 > nx or nx > n - 1 or ny < 0 or ny > n-1:
                continue
            if visited[nx][ny] == 0:
                if board[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny]= 1
                    distance[nx][ny] += distance[cur_x][cur_y] + 1
                    if board[nx][ny] < shark_size and board[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))
while 1:
    shark = eat_fish(shark_x,shark_y, shark_size)
    if len(shark) == 0:
        break
    nx,ny,dist = shark.pop()
    result += dist
    board[nx][ny] = 0
    shark_x,shark_y = nx,ny
    eat_count += 1
    if eat_count == shark_size:
        eat_count = 0
        shark_size += 1
print(result)


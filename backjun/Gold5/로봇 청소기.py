from collections import deque
n, m = map(int, input().split())
x, y, p = map(int,input().split())
q = deque()
q.append((x,y,p))
tmp = []
left = [[0,-1], [-1,0],[0,1], [1,0]]
back = [[1,0], [0,-1], [-1,0],[0,1]]
visited = [[False]*m for _ in range(n)]
visited[x][y] = True
for _ in range(n):
    tmp.append(list(map(int, input().split())))
board = [[1] * (m+2) for _ in range(n+2)]
for i in range(n):
    for j in range(m):
        board[i+1][j+1] = tmp[i][j]
del tmp
count = 0
answer = 1
while True:
    next_x, next_y = x + left[p][0], y + left[p][1]
    #청소 공간 존재
    if visited[next_x][next_y] is False and board[next_x + 1][next_y + 1] == 0:
        x, y = next_x, next_y
        visited[x][y] = True
        answer += 1
        count = 0
        if p == 0:
            p = 3
        else:
            p -= 1
        continue
    #청소공간 없음 회전만
    else:
        if p == 0:
            p = 3
        else:
            p -= 1
        count += 1
    # 회전만 4번 한 경우
    if count == 4:
        next_x, next_y = x+back[p][0], y + back[p][1]
        #벽인경우는 break
        if board[next_x+1][next_y+1] == 1:
            break
        else: #벽이 아니면 후진
            x, y = next_x, next_y
            visited[x][y] = True
            count = 0
print(answer)
from collections import deque
import sys
def bfs(board, visited,position):
    x, y = position
    q = deque()
    q.append((x,y,0))
    visited[x][y] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while len(q) != 0:
        x, y, count = q.popleft()
        for i in range(4):
            import sys
            from collections import deque
            m, n, h = map(int, input().split())  # mn크기, h상자수
            graph = []
            queue = deque([])

            for i in range(h):
                tmp = []
                for j in range(n):
                    tmp.append(list(map(int, sys.stdin.readline().split())))
                    for k in range(m):
                        if tmp[j][k] == 1:
                            queue.append([i, j, k])
                graph.append(tmp)

            dx = [-1, 1, 0, 0, 0, 0]
            dy = [0, 0, 1, -1, 0, 0]
            dz = [0, 0, 0, 0, 1, -1]
            while (queue):
                x, y, z = queue.popleft()

                for i in range(6):
                    a = x + dx[i]
                    b = y + dy[i]
                    c = z + dz[i]
                    if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
                        queue.append([a, b, c])
                        graph[a][b][c] = graph[x][y][z] + 1

            day = 0
            for i in graph:
                for j in i:
                    for k in j:
                        if k == 0:
                            print(-1)
                            exit(0)
                    day = max(day, max(j))
            print(day - 1)
            next_x, next_y = x + dx[i], y + dy[i]
            if next_x < 0 or next_x > len(board) - 1 or next_y < 0 or next_y > len(board[0]) - 1:
                continue
            if visited[next_x][next_y] == -1 and board[next_x][next_y] != -1:
                visited[next_x][next_y] = count + 1
                q.append((next_x, next_y, count + 1))
            elif visited[next_x][next_y] > count + 1:
                q.append((next_x,next_y,count+1))
                visited[next_x][next_y] = count + 1

m, n = map(int,sys.stdin.readline().split())
board = []
day = 0
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
             bfs(board,visited, [i,j])
        elif board[i][j] == -1:
            visited[i][j] = -2
check = True
for i in range(n):
    if -1 in visited[i]:
        check = False
    else:
        day = max(day, max(visited[i]))

if check:
    print(day)
else:
    print(-1)

#입력받는 형식때문에 시간초과가 계속 났었다. 논리자체는 틀린게 없다 가끔 백준은 이런것때문에 화가나는 부분도 있다.
#다른사람의 코드를 보니 다른 bfs진행이나 모든형식이 같으나 입력받을때 1인 부분의 인덱스를 기억해두고 저장하여 board를 순회하는 부분 떄문에 시간초과가 났었다.
#프로그래머스에서는 불가능한 방식이므로 굳이 생각안해도된다.
# 이런부분떄문에 백준이 가끔 좀...
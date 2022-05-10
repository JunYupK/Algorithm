from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    #맵의 테두리를 0으로 채우는 태크닉
    board = [[0]* (len(maps[0])+2) for _ in range(len(maps)+2)]
    visited = [[False]* len(maps[0])for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            board[i+1][j+1] = maps[i][j]
    #bfs를 위한 deque 첫 위치는 1,1 (index)
    q = deque()
    q.append((1,1))
    visited[0][0] = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]  # 상하좌우
    maps[0][0] = 1
    while len(q) != 0:
        x, y = q.popleft()
        next_pos = []
        # 상하좌우 체크
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if board[next_x][next_y] == 1:
                next_pos.append((next_x, next_y))
        for next in next_pos:
            if visited[next[0]-1][next[1]-1] is False:
                visited[next[0] - 1][next[1] - 1] = True
                q.append(next)
                maps[next[0] -1 ][next[1]-1] = maps[x-1][y-1] + 1

    answer = maps[n-1][m-1]
    if answer == 1:
        answer = -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
solution(maps)

#BFS 로 n,n의 위치를 탐색할때 먼저 도착하는경우가 최단거리라는 거를 기억하자 그냥 bfs로 목표 위치에 도착하면 최단거리!
#또한 효율성 관련에서 visited를 보통 리스트로 관리 해왔었는데 이 경우 n의 시간이 걸리는데 이 부분때문에 효율성에서 시간초과가 떴다...좀 빡빡한 경우에는 visited를 배열로 구현하자
from collections import deque
def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    start,lever, end = (0,0),(0,0),(0,0)
    moves = [(0,-1), (0,1), (-1,0), (1,0)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = (i,j)
                break

    def bfs(start, target):
        q = deque()
        visited = [[False] * M for _ in range(N)]
        q.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = True
        while q:
            x, y, count = q.popleft()
            if maps[x][y] == target:
                return (x,y, count)
            for dx,dy in moves:
                nx, ny = dx + x, dy + y
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] is False and maps[nx][ny] != 'X':
                        q.append((nx,ny,count+1))
                        visited[nx][ny] = True
        return (-1,-1,-1)
    result = bfs(start,'L')
    if result[2] == -1:
        return -1
    answer = bfs((result[0],result[1]), 'E')
    if answer[2] == -1:
        return -1
    else:
        return result[2] + answer[2]

print(solution(["SOOOO", "XXXXO", "OOOOO", "OXXXX", "OOOLE"]))
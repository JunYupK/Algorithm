from sys import stdin
move = [(0,1), (0, -1), (1, 0), (-1, 0)]
N,M = map(int, input().split())
board = [list(map(int,input().split()))for _ in range(N)]
visited = [[False] * N for _ in range(N)]

maxValue = 0
def dfs(i, j, dsum, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt + 1)
            visited[ni][nj] = False
def exce(i, j):
    global maxValue
    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
            t = (n+k)%4
            ni = i + move[t][0]
            nj = j + move[t][1]
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        maxValue = max(maxValue, tmp)
for i in range(N):
    for j in range(N):
        visited[i][j] = True
        dfs(i,j, board[i][j], 1)
        visited[i][j] = False
        exce(i, j)

print(maxValue)
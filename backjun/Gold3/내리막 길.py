import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

M,N = map(int,input().split())
board = []
moves = [(-1,0), (1,0), (0,-1), (0,1)]
dp = [[-1] * N for _ in range(M)]
for _ in range(M):
    arr = list(map(int, input().split()))
    board.append(arr)
def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    ways = 0
    for dx, dy in moves:
        nx, ny = dx + x , y + dy
        if 0 <= nx < M and 0 <= ny < N and board[x][y] > board[nx][ny]:
            ways += dfs(nx,ny)
    dp[x][y] = ways
    return dp[x][y]
print(dfs(0,0))
for i in range(M):
    print(dp[i])

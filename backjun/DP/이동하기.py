import sys
input = sys.stdin.readline
N, M = map(int,input().split())
answer = 0
board = []
dp = [[0] * M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
dp[0][0] = board[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + board[0][i]

for i in range(1,N):
    for j in range(M):
        if j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
            continue
        dp[i][j] += max(board[i][j] + dp[i-1][j], board[i][j] + dp[i][j-1])

print(dp[N-1][M-1])
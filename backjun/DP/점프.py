import sys
input = sys.stdin.readline
N = int(input())
dp = [[0] * N for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            break
        next_x1, next_y1 = i + board[i][j], j
        next_x2, next_y2 = i, j + board[i][j]
        if 0 <= next_x1 < N and 0 <= next_y1 < N:
            dp[next_x1][next_y1] += dp[i][j]
        if 0 <= next_x2 < N and 0 <= next_y2 < N:
            dp[next_x2][next_y2] += dp[i][j]

print(dp[N-1][N-1])
N = int(input())
dp = [[0]* (N+1) for _ in range(2)]
dp[1][0] = 1
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
    dp[1][i] = dp[0][i-1]
print(dp[0][N-1] + dp[1][N-1])
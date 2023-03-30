import sys
input = sys.stdin.readline
n, k = map(int,input().split())
dp = [[0] * (n+1) for _ in range(k+1)]
for i in range(n+1):
    dp[0][i] = 1
for i in range(1, k+1):
    for j in range(n+1):
        dp[i][j] = sum(dp[i-1][0:j+1])

print(dp[k-1][n] % 1000000000)
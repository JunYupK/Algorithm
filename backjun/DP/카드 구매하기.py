N = int(input())
sales = list(map(int,input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[1][i] = i * sales[0]
for i in range(2, N+1):
    for j in range(1, N+1):
        if j < i:
            dp[i][j] = dp[i-1][j]
        elif j == i:
            dp[i][j] = max(sales[j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i-1][j], sales[i-1] + dp[i][j-i])

print(dp[N][N])
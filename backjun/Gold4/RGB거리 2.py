import sys

input = sys.stdin.readline
N = int(input())
data = []
result, INF = 1e9, 1e9
for _ in range(N):
    data.append(list(map(int,input().split())))

for color in range(3):
    dp = [[0 for _ in range(3)] for _ in range(N)]
    for i in range(3):
        if i == color:
            dp[0][i] = data[0][i]
        else:
            dp[0][i] = INF
    for i in range(1, N):
        dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])
    for i in range(3):
        if i != color:
            result = min(result, dp[-1][i])

print(result)
n, k = map(int,input().split())
tool = [[0,0]]
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    tool.append(list(map(int,input().split())))

for i in range(1, n +1):
    for j in range(1, k + 1):
        w = tool[i][0]
        v = tool[i][1]
        if j < w: #j가 배낭무게 w는 무게
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
    for d in dp:
        print(d)
    print()
print(dp[n][k])
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
matrix = []
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + arr[j]
    matrix.append(arr)

for i in range(2, N+1):
    for j in range(1, N+1):
        dp[i][j] += dp[i-1][j]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    result = dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2]) + dp[x1-1][y1-1]
    print(result)
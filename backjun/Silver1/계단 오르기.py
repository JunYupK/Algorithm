import sys
n = int(sys.stdin.readline())
stair = [0] * 301
dp = [0] * 301
for i in range(n):
    tmp = int(sys.stdin.readline())
    stair[i] = tmp
dp[0] = stair[0]
dp[1] = max(stair[0] + stair[1], stair[1])
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
for i in range(3,n):
    dp[i] = max(dp[i-2] + stair[i], stair[i-1]+ stair[i] + dp[i-3])
print(dp[n-1])
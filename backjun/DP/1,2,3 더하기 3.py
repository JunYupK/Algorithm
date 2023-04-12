import sys
input = sys.stdin.readline
T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for num in arr:
    print(dp[num])
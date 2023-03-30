import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)
dp = [10001] * (k+1)
dp[0] = 0

for num in coins:
    for i in range(num,k+1):
        dp[i] = min(dp[i], dp[i-num]+1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
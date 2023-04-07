N = int(input())
a = list(map(int,input().split()))
dp = [0] * N
dp[0] = a[0]
for i in range(1, N):
    dp[i] = max(dp[i-1]+a[i], a[i])
print(max(dp))
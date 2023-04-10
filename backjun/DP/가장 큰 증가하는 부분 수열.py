N = int(input())
a = list(map(int,input().split()))
dp = [0] * (N)
for i in range(N):
    dp[i] = a[i]
for i in range(N):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]
print(max(dp))
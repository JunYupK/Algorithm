import sys
input = sys.stdin.readline
n = int(input())
dp = [1] * n
arr = list(map(int,input().split()))
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
_max = max(dp)
result = []
for i in range(n-1,-1,-1):
    if dp[i] == _max:
        result.append(arr[i])
        _max -= 1
result.reverse()
print(*result)
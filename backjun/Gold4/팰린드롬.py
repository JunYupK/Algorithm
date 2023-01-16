import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]
M = int(input())
for i in range(N):
    for start in range(N - i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif arr[start] == arr[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])

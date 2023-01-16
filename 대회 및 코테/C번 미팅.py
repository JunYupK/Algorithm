import sys

input = sys.stdin.readline

mbti = []
N, M, C = map(int, input().split())
for _ in range(C):
    mbti.append(list(map(int, input().split())))

studentA = list(map(int, input().split()))
studentB = list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + max(mbti[studentA[i - 1] - 1][studentB[j - 1] - 1],
                                              mbti[studentB[j - 1] - 1][studentA[i - 1] - 1]), dp[i - 1][j])
# for i in range(N + 1):
#     print(dp[i])
print(dp[N][M])

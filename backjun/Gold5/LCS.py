s1 = input()
s2 = input()
dp = [[0] * 1002 for _ in range(1002)]

for i in range(1, len(s2)+1):
    for j in range(len(s1)):
        if s1[j] == s2[i-1]:
            if j > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            elif j == 0:
                dp[i][j] = 1
        else:
            if j > 0:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            elif j == 0:
                dp[i][j] = dp[i-1][j]
print(dp[len(s2)][len(s1)-1])
# for i in range(len(s1)+1):
#     for j in range(len(s1)):
#         print(dp[i][j], end=" ")
#     print()


n = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3
for i in range(2, 31, 2):
    result = 0
    tmp = i - 2
    result = dp[tmp] * dp[2]
    while tmp != 0:
        tmp -= 2
        result += dp[tmp] * 2
    dp[i] = result
print(dp[n])
s1 = input()
s2 = input()
dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
for i in range(1,len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
x, y = len(s2), len(s1)
answer = ""
while x > 0 and y > 0:
    if s2[x-1] == s1[y-1]:
        answer += s2[x - 1]
        x, y = x-1, y-1
    else:
        if dp[x][y-1] > dp[x-1][y]:
            y -= 1
        else:
            x -= 1
if len(answer) == 0:
    print(len(answer))

else:
    print(len(answer))
    print(answer[::-1])
from collections import deque
N = int(input())
result = [[0, []] for _ in range(N+1)]
result[1][0] = 0
result[1][1] = [1]
for i in range(2, N + 1):
    result[i][0]= result[i-1][0] + 1
    result[i][1] = result[i-1][1] + [i]
    if i%3 == 0 and result[i//3][0] + 1 < result[i][0]:
        result[i][0] = result[i//3][0] + 1
        result[i][1] = result[i//3][1] + [i]
    if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
        result[i][0] = result[i // 2][0] + 1
        result[i][1] = result[i // 2][1] + [i]
print(result[N][0])
print(*result[N][1][::-1])
import sys
sys.stdin.readline
N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (1 << N -1) for _ in range(N)]
def tsp(i, route):
    if dp[i][route] != 0:
        return dp[i][route]
    if route == (1<<(N-1)) - 1:
        if W[i][0]:
            return W[i][0]
        else:
            return float('inf')
    min_route = float('inf')

    for j in range(1, N):
        if not W[i][j]:
            continue
        if route & (1<<j-1):
            continue
        D = W[i][j] + tsp(j, route | (1 << (j-1)))
        if min_route > D:
            min_route = D
    dp[i][route] = min_route
    return min_route
print(tsp(0,0))

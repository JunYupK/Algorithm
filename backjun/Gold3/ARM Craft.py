import sys
from collections import deque
sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    building = list(map(int, input().split()))
    enter = [0] * (N+1)
    dp = [0] * (N+1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        a, b = map(int,input().split())
        graph[a].append(b)
        enter[b] += 1
    target = int(input())
    #위상 정렬
    q = deque()
    for i in range(1,N+1):
        if enter[i] == 0:
            q.append(i)
            dp[i] = building[i-1]
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            enter[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[node] +building[next_node-1])
            if enter[next_node] == 0:
                q.append(next_node)
    print(dp[target])


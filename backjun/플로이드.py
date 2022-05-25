from collections import deque
INF = int(1e9)
n = int(input())
m = int(input())
adj = []
edges = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a== b:
            edges[a][b] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < edges[a][b]:
        edges[a][b] = c

for k in range(1 , n+1):
    for a in range(1, n +1):
        for b in range(1, n+1):
            edges[a][b] = min(edges[a][b], edges[a][k] + edges[k][b])

for a in range(1, n +1):
    for b in range(1, n+1):
        if edges[a][b] == INF:
            print(0, end=" ")
        else:
            print(edges[a][b], end=" ")
    print()

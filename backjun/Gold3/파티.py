import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m, x = map(int,input().split())
city = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int,input().split())
    city[s].append((e,t))

for c in city:
    c.sort(key=lambda x:x[1])

def dijkstra(start):
    visited = [1e9] * (n+1)
    visited[start] = 0
    q = []
    heapq.heappush(q,[0,start])
    while q:
        print(q)
        w, node = heapq.heappop(q)
        if visited[node] < w:
            continue
        for idx, node_cost in city[node]:
            cost = w + node_cost
            if visited[idx] > cost:
                visited[idx] = cost
                heapq.heappush(q,(cost,idx))
    return visited
result = 0
# for i in range(1, n+1):
#     go = dijkstra(i)
#     back = dijkstra(x)
#     result = max(result, go[x] + back[i])
# print(result)

dijkstra(2)
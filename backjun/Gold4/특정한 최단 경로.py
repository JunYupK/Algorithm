import sys
import heapq
from collections import deque
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    s, e, t = map(int,input().split())
    graph[s].append((e, t))
    graph[e].append((s, t))

v1, v2 = map(int, input().split())

def dilkstra(start):
    distance = [1e9] * (N+1)
    distance[0] = 0
    distance[start] = 0
    q = []
    heapq.heappush(q,(0, start))

    while q:
        dist, node = heapq.heappop(q)
        for node_idx, node_cost in graph[node]:
            cost = node_cost + dist
            if distance[node_idx] > cost:
                distance[node_idx] = cost
                heapq.heappush(q,(cost, node_idx))

    return distance

startDist = dilkstra(1)
v1Dist = dilkstra(v1)
v2Dist = dilkstra(v2)
answer = min(startDist[v1]+v1Dist[v2]+v2Dist[N], startDist[v2]+v2Dist[v1]+v1Dist[N])
print(startDist)
print(v1Dist)
print(v2Dist)
if answer >= 1e9:
    print(-1)
else:
    print(answer)
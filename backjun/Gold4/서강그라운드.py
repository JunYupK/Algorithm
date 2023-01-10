import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b, cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
def dijkstra(start):
    dist = [1e9] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        w, node = heapq.heappop(q)
        for idx, road in graph[node]:
            current = w + road
            if dist[idx] > current:
                dist[idx] = current
                heapq.heappush(q,(current, idx))
    return dist
result = []
for i in range(n):
    tmp = 0
    distance = dijkstra(i+1)
    for j in range(1,n+1):
        if distance[j] <= m:
            tmp += items[j-1]
    result.append(tmp)
print(max(result))

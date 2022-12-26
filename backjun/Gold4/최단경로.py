import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))
def dilkstra(start):
    distance = [1e9] * (V+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost, node = heapq.heappop(q)
        for node_idx, node_cost in graph[node]:
            cur_cost = cost + node_cost
            if distance[node_idx] > cur_cost:
                distance[node_idx] = cur_cost
                heapq.heappush(q, (cur_cost, node_idx))
    return distance

result = dilkstra(K)
for i in range(1,V+1):
    if result[i] == 1e9:
        print("INF")
    else:
        print(result[i])
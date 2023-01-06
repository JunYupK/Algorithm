import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
start, end = map(int,input().split())
def dijkstra(start, end):
    distance = [1e9] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start, [start]))
    while q:
        node_cost, node_idx, road = heapq.heappop(q)
        if node_idx == end:
            return distance, road
        for idx ,weight in graph[node_idx]:
            tmp_cost = node_cost + weight
            if distance[idx] > tmp_cost:
                distance[idx] = tmp_cost
                heapq.heappush(q, (tmp_cost, idx, road+[idx]))
dist, route = dijkstra(start, end)
print(dist[end])
print(len(route))
print(*route)

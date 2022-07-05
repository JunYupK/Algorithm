import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    tmp = list(map(int,list(map(int,sys.stdin.readline().split()))))
    graph[tmp[0]].append((tmp[1],tmp[2]))
start, end = map(int, input().split())
INF = 1e9
visited = [False] * (n+1)
distance = [INF] * (n+1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = min(distance[j[0]],j[1])
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)
print(distance[end])
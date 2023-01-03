import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    _max = [0, 0]
    while q:
        print(visited)
        node = q.popleft()
        for next_node, next_cost in graph[node]:
            if visited[next_node] is False:
                visited[next_node] = next_cost + visited[node]
                q.append(next_node)
                if _max[0] < visited[next_node]:
                    _max = visited[next_node],next_node
    return _max
cost, node = bfs(1)
cost, node = bfs(node)
print(cost)
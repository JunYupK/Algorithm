from collections import deque
def BFS(n, edges , v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        data = q.popleft()
        print(data, end=" ")
        for i, j in edges:
            if data == i:
                if visited[j] == False:
                    visited[j] = True
                    q.append(j)


def DFS(n, edges, v, visited):

    print(v, end=' ')
    visited[v] = True

    for i, j in edges:
        if i == v:
            if visited[j] is False:
                DFS(n,edges, j, visited)
    return

n, m, v = map(int, input().split())
edges = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    edges.append([tmp[0], tmp[1]])
    edges.append([tmp[1], tmp[0]])

edges = sorted(edges,key=lambda x:x[1])
visited = [False] * (n + 1)
DFS(n, edges,v, visited)
visited = [False] * (n + 1)
print()
BFS(n,edges,v, visited)
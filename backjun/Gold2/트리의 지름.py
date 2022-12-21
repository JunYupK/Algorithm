import sys
from collections import deque
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    line = list(map(int,input().split()))
    for i in range(1,len(line)):
        if(line[i] == -1):
            break
        if(i%2 == 0):
            graph[line[0]].append((line[i-1],line[i]))

def bfs(start):
    visited = [False] * (V+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    _max = [0,0]
    while q:
        x = q.popleft()
        for y, w in graph[x]:
            if visited[y] is False:
                visited[y] = visited[x] + w
                q.append(y)
                if _max[0] < visited[y]:
                    _max = visited[y],y
    return _max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
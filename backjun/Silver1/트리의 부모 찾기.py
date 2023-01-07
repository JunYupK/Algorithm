import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (n+1)
def bfs(start):
    q = deque()
    visited = [False] * (n + 1)
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        for next in tree[node]:
            if visited[next] is False:
                q.append(next)
                visited[next] = True
                parents[next] = node
bfs(1)
for i in range(2,n+1):
    print(parents[i])
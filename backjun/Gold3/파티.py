import sys
from collections import deque
input = sys.stdin.readline

n, m, x = map(int,input().split())
city = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int,input().split())
    city[s].append((e,t))

print(city)
def bfs(start, destination):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    _min = [0,0]
    while q:
        tmp = q.popleft()
        if tmp == destination:
            return visited[tmp]
        for y, w in city[tmp]:
            if visited[y] == -1:
                visited[y] = visited[tmp] + w
                q.append(y)
                if _min[0] == 0:
                    _min = visited[y],y
                    continue
                if _min[0] > visited[y]:
                    _min = visited[y], y

for i in range(1, n+1):
    print(bfs(i,2))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in range(1, n+1):
    print(bfs(x,i))
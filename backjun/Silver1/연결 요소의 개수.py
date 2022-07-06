import sys
from collections import deque
n, m = map(int,input().split())
lines = []
edges = [False] * (n+1)
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    lines.append((x,y))
    lines.append((y,x))
answer = 0
for i in range(1,n+1):
    if edges[i] is False:
        answer += 1
        q = deque()
        q.append(i)
        edges[i] = True
        while q:
            data = q.popleft()
            for x,y in lines:
                if data == x and edges[y] is False:
                    edges[y] = True
                    q.append(y)

print(answer)
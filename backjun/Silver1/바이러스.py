import sys
from collections import deque
n = int(input())
t = int(input())
visited = [False] * (n+1)
lines = []
q = deque()
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    lines.append((x,y))
    lines.append((y,x))
answer = 0
visited[1] = True
q.append(1)
while q:
    data = q.popleft()
    for next_x, next_y in lines:
        if next_x == data and visited[next_y] is False:
            q.append(next_y)
            visited[next_y] = True
            answer += 1
print(answer)
from collections import deque
n, k = map(int, input().split())
q = deque()
time = 0
visited = [False] * 100001
q.append((n, time))
while q:
    position , time = q.popleft()
    if position == k:
        print(time)
        break

    if  position * 2 <= 100000 and visited[position*2] is False:
        q.append((position*2, time + 1))
        visited[position * 2] = True
    if  position + 1 <= 100000 and visited[position + 1] is False:
        q.append((position + 1, time + 1))
        visited[position + 1] = True
    if position -1 >= 0 and visited[position - 1] is False:
        q.append((position - 1, time + 1))
        visited[position-1] = True

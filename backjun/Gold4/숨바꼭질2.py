import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int,input().split())

def bfs(start, end):
    visited = [False] * 100001
    visited[start]= True
    q = deque()
    q.append((0,start))
    answer = []
    while q:
        cost, pos = q.popleft()
        visited[pos] = True
        if pos == end:
            answer.append(cost)
        if 0 <= pos * 2 <= 100000 and visited[pos*2] is False:
            q.append((cost+1, pos*2))
        if 0 <= pos + 1 <= 100000 and visited[pos + 1] is False:
            q.append((cost+1,pos+1))
        if 0 <= pos - 1 <= 100000 and visited[pos-1] is False:
            q.append((cost+1, pos-1))
    return answer
result = bfs(N, K)
print(result[0])
print(result.count(min(result)))
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1):
        in_degree[tmp[i+1]] += 1
        graph[tmp[i]].append(tmp[i+1])


def bfs():
    q = deque()
    result = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        next_idx = q.popleft()
        result.append(next_idx)
        for x in graph[next_idx]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                q.append(x)
    if sum(in_degree) > 0:  # 순서 정하는 게 불가능한 경우
        print(0)
    else:
        [print(i) for i in result]
bfs()

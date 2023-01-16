import sys
input = sys.stdin.readline
N, M = map(int,input().split())
parents = list( i for i in range(N+1))
edges = []
for _ in range(M):
    edges.append(list(map(int,input().split())))
edges.sort(key=lambda x:x[2])
def find_parent(node):
    if parents[node] != node:
        parents[node] = find_parent(parents[node])
    return parents[node]
def union(a,b):
    rootA = find_parent(a)
    rootB = find_parent(b)
    if rootA == rootB:
        return
    elif rootA > rootB:
        parents[rootA] = rootB
    else:
        parents[rootB] = rootA
answer = 0
_max = 0
for a,b,cost in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        answer += cost
        if _max < cost:
            _max = cost
print(answer - _max)
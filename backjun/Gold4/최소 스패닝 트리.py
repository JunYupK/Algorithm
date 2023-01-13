import sys
input = sys.stdin.readline
V, E = map(int,input().split())
edges = []
parents = list(i for i in range(V+1))
for _ in range(E):
    a, b, cost = map(int,input().split())
    edges.append((a,b,cost))
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
    if rootA > rootB:
        parents[rootA] = rootB
    else:
        parents[rootB] = rootA
total = 0
for a,b,cost in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        total += cost
print(total)
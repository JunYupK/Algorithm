def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
answer = 0
for _ in range(m):
    edges.append(list(map(int, input().split())))
edges = sorted(edges, key=lambda x:x[2])
mst = []
for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        mst.append([a,b,cost])
        answer += cost
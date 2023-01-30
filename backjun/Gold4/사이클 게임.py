import sys
sys.stdin.readline
n, m = map(int,input().split())
parents = [i for i in range(n)]
answer = 0
def find_root(node):
    if node == parents[node]:
        return node
    else:
        parents[node] = find_root(parents[node])
        return parents[node]
def union(a, b):
    a = find_root(a)
    b = find_root(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
for i in range(m):
    x, y = map(int,input().split())
    if find_root(x) == find_root(y):
        print(i+1)
        exit(0)
    union(x,y)
else:
    print(0)


import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
planets = []
edges = []
parents = list(i for i in range(N))
for i in range(N):
    planets.append((list(map(int,input().split())), i))
planets.sort(key=lambda x:x[0][0])
for i in range(1,N):
    cost = abs(planets[i][0][0] - planets[i-1][0][0])
    edges.append((planets[i-1][1], planets[i][1] , cost))
planets.sort(key = lambda x:x[0][1])
for i in range(1,N):
    cost = abs(planets[i][0][1] - planets[i-1][0][1])
    edges.append((planets[i-1][1], planets[i][1] , cost))
planets.sort(key = lambda x:x[0][2])
for i in range(1,N):
    cost = abs(planets[i][0][2] - planets[i-1][0][2])
    edges.append((planets[i-1][1], planets[i][1] , cost))
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
for a,b,cost in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        answer += cost
print(answer)
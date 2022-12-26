import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    edges = []
    for _ in range(M):
        u, v, w = map(int,input().split())
        edges.append((u,v,w))
        edges.append((v, u, w))
    for _ in range(W):
        S, E, T = map(int,input().split())
        edges.append((S,E,-T))
    distance = [1e9] * (N + 1)
    def bellman_ford(start):
        distance[start] = 0
        for i in range(1,(N+1)):
            for edge in edges:
                cur_node = edge[0]
                next_node = edge[1]
                node_cost = edge[2]
                if distance[next_node] > distance[cur_node] + node_cost:
                    distance[next_node] = distance[cur_node] + node_cost
                    if i == N:
                        return True
        return False
    cycle = bellman_ford(1)
    if cycle:
        print("YES")
    else:
        print("NO")

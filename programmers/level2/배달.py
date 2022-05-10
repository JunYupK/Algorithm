# import heapq
# def dijkstra(edges, adj):
#     heap = []
#     heapq.heappush(heap, [0,1])
#     while heap:
#         weight, edge = heapq.heappop(heap)
#         for w, e in adj[edge]:
#             if weight + w < edges[e]:
#                 edges[e] = weight + w
#                 heapq.heappush(heap, [weight + w, e])
#
# def solution(N, road, K):
#     edges = [1e9]*(N+1)
#     adj = [[] for _ in range(N+1)]
#     edges[1] = 0
#     for data in road:
#         adj[data[0]].append([data[2], data[1]])
#         adj[data[1]].append([data[2], data[0]])
#     dijkstra(edges, adj)
#     return len([x for x in edges if x<=K])
#
# N = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K = 3
# solution(N,road,K)
#
# #전형적인 다익스트라 알고리즘문제.. 이것도 제대로 구현 못했다 반성하고 다시한번 보도록 하자

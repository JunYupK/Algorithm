import heapq
def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a,b,w in paths:
        graph[a].append((b,w))
        graph[b].append((a,w))
    summits.sort()
    summits_set = set(summits)
    def dijkstra():
        q = []
        distance = [1e9] * (n+1)
        for gate in gates:
            distance[gate] = 0
            heapq.heappush(q, (0, gate))
        while q:
            cost, idx = heapq.heappop(q)
            if idx in summits:
                continue
            for next_node, next_cost in graph[idx]:
                new_cost = max(cost, next_cost)
                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))
        result = [0, 1e9]
        for summit in summits:
            if distance[summit] < result[1]:
                result[0] = summit
                result[1] = distance[summit]
        return result
    return dijkstra()

solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]
)
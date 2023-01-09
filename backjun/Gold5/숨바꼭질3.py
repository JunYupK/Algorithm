import heapq


def dijkstra(cost, start):
    cost[start] = 0
    qu = []
    heapq.heappush(qu, [cost[start], start])

    while qu:
        cur_cost, cur_dest = heapq.heappop(qu)

        if cost[cur_dest] < cur_cost:
            continue

        if cur_dest <= 50000:
            if cur_cost < cost[cur_dest * 2]:
                cost[cur_dest * 2] = cur_cost
                heapq.heappush(qu, [cur_cost, cur_dest * 2])
        if cur_dest < 100000:
            if cur_cost + 1 < cost[cur_dest + 1]:
                cost[cur_dest + 1] = cur_cost + 1
                heapq.heappush(qu, [cur_cost + 1, cur_dest + 1])
        if cur_dest > 0:
            if cur_cost + 1 < cost[cur_dest - 1]:
                cost[cur_dest - 1] = cur_cost + 1
                heapq.heappush(qu, [cur_cost + 1, cur_dest - 1])


N, K = map(int, input().split())
cost = [1e9 for _ in range(100001)]
dijkstra(cost, N)
print(cost[K])
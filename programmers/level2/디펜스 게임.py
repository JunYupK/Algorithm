import heapq
def solution(n, k, enemy):
    q = []
    tmp = 0
    for i, e in enumerate(enemy):
        heapq.heappush(q, -e)
        tmp += e
        if tmp > n:
            tmp += heapq.heappop(q)
            if k == 0:
                return i+1
            k -= 1
    return i+1
print(solution(7, 0, [8, 8, 8, 8, 8, 8, 8]))
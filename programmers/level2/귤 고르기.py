from collections import Counter
import heapq

def solution(k, tangerine):
    answer = 0
    tmp = Counter(tangerine)
    q = []
    for t in tmp:
        heapq.heappush(q, (tmp[t]))
    _sum = sum(q)
    while q:
        num = heapq.heappop(q)
        if _sum - num < k:
            return len(q) + 1
        elif _sum - num == k:
            return len(q)
        _sum -= num

    return answer
solution(3, [1, 3, 2, 5, 4, 5, 2, 3])
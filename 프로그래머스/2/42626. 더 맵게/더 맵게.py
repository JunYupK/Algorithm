import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for scov in scoville:
        heapq.heappush(q, scov)
    while q:
        cur = heapq.heappop(q)
        if cur >= K:
            break
        else:
            if len(q) == 0:
                answer = -1
                break
            next_food = heapq.heappop(q)
            cur = cur + (next_food * 2)
            heapq.heappush(q,cur)
        answer += 1
    print(q)      
    return answer
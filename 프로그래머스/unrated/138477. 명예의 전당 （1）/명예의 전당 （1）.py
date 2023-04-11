import heapq
def solution(k, score):
    answer = []
    q = []

    for i in range(len(score)):
        if i < k:
            heapq.heappush(q, score[i])
            answer.append(min(q))
        else:
            if q[0] < score[i]:
                heapq.heappop(q)
                heapq.heappush(q, score[i])
            answer.append(min(q))
            
    
    return answer
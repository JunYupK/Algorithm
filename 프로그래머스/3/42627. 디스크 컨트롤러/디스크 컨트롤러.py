import heapq
from collections import deque
def solution(jobs):
    answer = 0
    jobs.sort()
    q = deque(jobs)
    pq = []
    time = 0
    count = 0
    dummy = -1
    while count != len(jobs):
        while q:
            if q[0][0] <= time:
                start, cost = q.popleft()
                heapq.heappush(pq, (cost,start)) 
            else:
                break
        if(pq):
            cost, start = heapq.heappop(pq)
            time += cost
            answer += time - start
            count += 1
        else:
            time += 1
    print(answer)    
    return answer//len(jobs)
import heapq
def solution(jobs):
    answer = 0
    i = 0
    start = -1
    q = []
    time = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(q, (j[1],j[0]))
        if len(q) > 0:
            cost ,s = heapq.heappop(q)
            start = time
            time += cost
            answer += time - s
            i += 1
        else:
            time += 1

    return answer // len(jobs)

jobs = [[0, 10], [1,10],[11,10]]
print(solution(jobs))
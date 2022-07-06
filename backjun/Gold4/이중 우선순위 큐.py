import sys
from collections import deque
import heapq
n = int(input())

#최소힙 최대힙 모두 사이즈가 0 인 경우 최대힙에 삽입
#만약 최대힙의 top보다 큰 값인경우 최대힙에 삽입
#최대합의 top보다 작은 경우에는 최소힙에 삽입
for _ in range(n):
    t = int(input())
    minq = []
    maxq = []
    visited = {}
    id = 0
    for _ in range(t):
        tmp = sys.stdin.readline().split()
        if tmp[0] == 'I':
            num = int(tmp[1])
            id += 1
            heapq.heappush(maxq,(-num, id))
            heapq.heappush(minq,(num,id))
        elif tmp[0] == 'D':
            num = int(tmp[1])
            if num == 1 and len(maxq) != 0:
                while maxq and maxq[0][1] in visited:
                    heapq.heappop(maxq)
                if len(maxq) != 0:
                    x = heapq.heappop(maxq)
                    visited[x[1]] = True
            elif minq and num == -1 and len(minq) != 0:
                while minq and minq[0][1] in visited:
                    heapq.heappop(minq)
                if len(minq) != 0:
                    x = heapq.heappop(minq)
                    visited[x[1]] = True
        # print(maxq, minq)
        # print(visited)
        # print()
    while maxq and maxq[0][1] in visited:
        heapq.heappop(maxq)
    while minq and minq[0][1] in visited:
        heapq.heappop(minq)
    if len(maxq) == 0 or len(minq) == 0:
        print("EMPTY")
    else:
        a = -maxq[0][0]
        b = minq[0][0]
        print(a,b)
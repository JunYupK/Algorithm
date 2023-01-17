import sys
import heapq
input = sys.stdin.readline
N, K = map(int,input().split())
jewel = []
bags = []
for _ in range(N):
    heapq.heappush(jewel, list(map(int,input().split())))
for _ in range(K):
    bags.append(int(input()))
bags.sort()
answer = 0
tmp = []
for bag in bags:
    while jewel and jewel[0][0] <= bag:
        weight, cost = heapq.heappop(jewel)
        heapq.heappush(tmp, -cost)
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jewel:
        break
print(answer)
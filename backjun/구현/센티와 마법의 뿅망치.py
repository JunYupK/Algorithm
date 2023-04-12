import sys
import heapq
input = sys.stdin.readline
N, H, T = map(int,input().split())
giant = []
tmp = T
for _ in range(N):
    heapq.heappush(giant, -int(input()))
while tmp != 0:
    x = -heapq.heappop(giant)
    if x == 1:
        heapq.heappush(giant, -x)
        break
    if x < H:
        heapq.heappush(giant, -x)
        break
    else:
        x = x // 2
        heapq.heappush(giant, -x)
        tmp -= 1

flag = -heapq.heappop(giant)
if flag >= H:
    print('NO')
    print(flag)
else:
    print('YES')
    print(T-tmp)
from bisect import bisect_left
import sys
n, c = map(int,input().split())
distance = []
for _ in range(n):
    distance.append(int(sys.stdin.readline()))
distance.sort()
result = 0
start = 1
end = distance[-1] - distance[0]
while start <= end:
    mid = (start + end) // 2
    val = distance[0]
    count = 1
    for i in range(1, len(distance)):
        if distance[i] >= val + mid:
            count += 1
            val = distance[i]
    if count >= c:
        start += 1
        result = mid
    else:
        end = mid - 1
print(result)

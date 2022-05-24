from bisect import bisect_left, bisect_right
n ,x = map(int, input().split())
data = list(map(int, input().split()))
count = bisect_right(data, x) - bisect_left(data, x)
if count > 0:
    print(count)
else:
    print(-1)
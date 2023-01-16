import sys
input = sys.stdin.readline
N, S = map(int,input().split())
arr = list(map(int,input().split()))
right = 0
interval_sum = 0
count = 0
_min = 1e9
for left in range(N):
    while interval_sum < S and right < N:
        interval_sum += arr[right]
        right += 1
    if interval_sum >= S and _min > right - left:
        _min = right - left
        count += 1
    interval_sum -= arr[left]

if count > 0:
    print(_min)
else:
    print(count)
from bisect import bisect_left, bisect_right
def binary_search(array, start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)
n = int(input())
a = list(map(int,input().split()))
start = 0
end = n - 1

while start < end:
    mid = (start + end) // 2
    if a[mid] == mid:
        print(mid)
        break
    elif a[mid] > mid:
        end = bisect_left(a, mid)
    else:
        start = bisect_right(a, mid)

if start >= end and mid != start and mid != end:
    print(-1)
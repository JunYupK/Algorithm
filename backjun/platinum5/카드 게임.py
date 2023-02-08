import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
select_num = list(map(int,input().split()))
sorted_num = sorted(numbers)
#left가 최대힙, right가 최소힙
mid = (len(select_num)-1)//2
left, right = [],[]
for i in range(M):
    heapq.heappush(right, sorted_num[i])
def find_maxmin(target):
    if len(left) == 0:
        tmp = heapq.heappop(right)
        heapq.heappush(left, -tmp)
    elif len(right) == 0:
        tmp = heapq.heappop(left)
        heapq.heappush(right, -tmp)
    while left and right:
        if -left[0] <= target < right[0]:
            print(right[0])
            heapq.heappop(right)
            return
        if -left[0] > target:
            tmp = heapq.heappop(left)
            heapq.heappush(right, -tmp)
        elif right[0] <= target:
            tmp = heapq.heappop(right)
            heapq.heappush(left, -tmp)

    if len(left) == 0:
        print(heapq.heappop(right))
    else:
        print(-heapq.heappop(left))
# def find_maxmin(target):
#     left = 0
#     right = len(sorted_num) - 1
#     tmp_arr = sorted_num
#     while left <= right:
#         mid = (left + right) // 2
#         if sorted_num[mid-1] <= target < sorted_num[mid+1] and target < sorted_num[mid]:
#             print(sorted_num[mid])
#             tmp_arr = sorted_num[0:mid] + sorted_num[mid+1:len(sorted_num)]
#             return tmp_arr
#         if sorted_num[mid] < target:
#             left = mid + 1
#         elif sorted_num[mid] >= target:
#             right = mid - 1
#     if left == 0:
#         print(sorted_num[0])
#         return sorted_num[1:len(sorted_num)]
#     else:
#         print(sorted_num[-1])
#         return sorted_num[0:len(sorted_num)-1]
for num in select_num:
    sorted_num = find_maxmin(num)


import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
left = [1] * N
right = [1] * N
count = 0
for i in range(1, N):
    if arr[i - 1] == arr[i] and arr[i] == 1:
        left[i] += left[i - 1]
    if arr[i - 1] == arr[i] and arr[i] == 2:
        right[i] += right[i - 1]
left_sum = 0
right_sum = 0
for i in range(1, N):
    if i == N - 1:
        if left[i] != 1:
            left_sum += left[i]
        if right[i] != 1:
            right_sum += right[i]
    if left[i - 1] > left[i]:
        left_sum += left[i - 1]
    if right[i - 1] > right[i]:
        right_sum += right[i - 1]
print(max(left_sum, right_sum))

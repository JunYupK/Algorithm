from collections import deque
from sys import stdin
D, N = map(int, stdin.readline().split())
oven = list(map(int, stdin.readline().split()))
pizza = list(map(int,stdin.readline().split()))
for i in range(1, len(oven)):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]
left , right = 0 , len(oven) - 1
pizza_check = 0
position = 0
for p in pizza:
    check = False
    while left <= right:
        mid = (left + right) // 2
        tmp = oven[mid]
        if tmp >= p:
            left = mid + 1
            position = mid
            check = True
        else:
            right = mid - 1
    if check is False:
        pizza_check = -1
        break
    left = 0
    right = position - 1

if pizza_check == -1:
    print(0)
else:
    print(position + 1)

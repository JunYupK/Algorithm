import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = []
answer = 'Possible'
for _ in range(N):
    tmp = list(input().split())
    q.append(deque(tmp))

target = input().split()
for t in target:
    flag = True
    for arr in q:
        if arr and arr[0] == t:
            arr.popleft()
            flag = False
    if flag:
        answer = 'Impossible'
        break
for arr in q:
    if len(arr) > 0:
        print('Impossible')
        exit(0)
print(answer)

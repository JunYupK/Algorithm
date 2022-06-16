from collections import deque
n, b = map(int,input().split())
result = deque()
while n != 0:
    tmp = n % b
    if tmp >= 10:
        tmp = chr(tmp + 55)
    result.append(str(tmp))
    n = n//b
result.reverse()
print("".join(list(result)))
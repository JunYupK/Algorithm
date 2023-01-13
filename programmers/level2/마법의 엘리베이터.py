from collections import deque
def solution(storey):
    count = len(str(storey))
    q = deque()
    q.append((0, storey))
    while q:
        print(q)
        num, target = q.popleft()
        if target < 0:
            continue
        if target == 0:
            return num
        tmp = 1
        for _ in range(count-1):
            q.append((num+1, target + tmp))
            q.append((num + 1, target - tmp))
            tmp *= 10

solution(1325)
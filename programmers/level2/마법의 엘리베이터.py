from collections import deque
_MAX = 100000000
def solution(storey):
    q = deque()
    q.append((storey, 0))
    visited = [False] * (_MAX + 1)
    while q:
        num, count = q.popleft()
        print(num)
        if num == 0:
            return count
        increment = 1
        while 1:
            tmp_num = increment + num
            if tmp_num > _MAX:
                break
            q.append((tmp_num, count + 1))
            increment *= 10




solution(1325)
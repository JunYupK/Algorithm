from collections import deque
_MAX = 1000000
def solution(x, y, n):
    answer = 0
    visited = [False] * _MAX
    q = deque()
    q.append((x, 0))
    while q:
        value, count = q.popleft()
        if value == y:
            return count
        if value + n < _MAX and visited[value+n] is False:
            visited[value + n] = True
            q.append((value+n , count+1))
        if value * 2 < _MAX and visited[value*2] is False:
            visited[value * 2] = True
            q.append((value*2, count +1))
        if value * 3 < _MAX and visited[value * 3] is False:
            visited[value * 3] = True
            q.append((value*3, count+1))
    return -1
print(solution(10,40,5))
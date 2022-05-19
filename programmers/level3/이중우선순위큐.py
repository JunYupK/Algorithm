from collections import deque
import heapq
def solution(operations):
    answer = []
    q = deque()
    for op in operations:
        op = op.split(' ')
        if op[0] == 'I':
            q.append(int(op[1]))
        else:
            if len(q) == 0:
                continue
            if op[1] == '1':
                q.pop()
            else:
                q.popleft()
        q = deque(sorted(q))

    if len(q) == 0:
        return [0,0]
    else:
        return [q.pop(), q.popleft()]

operations = ["I 16","D 1"]
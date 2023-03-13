from collections import deque
def solution(n, m, section):
    answer = 0
    q = deque()
    for sec in section:
        if q:
            if (sec - q[0]) - 1 > m:
                answer += 1
                q.clear()
            q.append(sec)
        else:
            q.append(sec)
    if q:
        answer += 1
    return answer
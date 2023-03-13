from collections import deque
def solution(A,B):
    answer = 0
    q1,q2 = deque(sorted(A,reverse=True)), deque(sorted(B, reverse=True))
    while q1 and q2:
        numA = q1[0] * q2[-1]
        numB = q1[-1] * q2[0]
        if numA > numB:
            answer += numA
            q1.popleft()
            q2.pop()
        else:
            answer += numB
            q1.pop()
            q2.popleft()
    return answer
solution([1, 4, 2], [5, 4, 4])
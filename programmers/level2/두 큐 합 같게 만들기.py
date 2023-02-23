from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    _sum = sum(queue1) + sum(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    target = _sum//2
    while q1 and q2:
        if q1_sum == q2_sum:
            return answer
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q1_sum -= num
            q2_sum += num
            q2.append(num)
        else:
            num = q2.popleft()
            q2_sum -= num
            q1_sum += num
            q1.append(num)
        answer += 1
        if answer >= 300000:
            break
    return -1
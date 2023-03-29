from collections import deque
def solution(s):
    answer = []
    q = deque(s)
    flag, count1, count2 = q[0],0,0
    tmp = ''
    while q:
        if count1 == count2 and count1 != 0:
            flag = q[0]
            answer.append(tmp)
            tmp = ''
        char = q.popleft()
        if char == flag:
            count1 += 1
        else:
            count2 += 1
        tmp += char
    if tmp != '':
        answer.append(tmp)
    return len(answer)
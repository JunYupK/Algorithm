from collections import deque
def is_perfect(s):
    stack = deque()
    dic = {'[': ']', '(':')', '{':'}'}
    for i in s:
        if i == '{' or i == '(' or i == '[':
            stack.append(i)
        elif i == ']' or i == '}' or i == ')':
            if len(stack) == 0:
                return False
            if dic[stack.pop()] != i:
                return False
    if len(stack) != 0:
        return False
    return True
def solution(s):
    answer = 0
    data = deque(s)
    if is_perfect(data) is True:
        answer += 1
    for i in range(len(s)-1):
        tmp = data.popleft()
        data.append(tmp)
        if is_perfect(data) is True:
            answer += 1
    return answer
s = "}]()[{"
print(solution(s))

#eeaassyy
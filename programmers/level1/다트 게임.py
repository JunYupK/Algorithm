from collections import deque
def solution(dartResult):
    answer = 0
    stack = deque()
    tmp = ''
    for char in dartResult:
        if char == 'S':
            stack.append(int(tmp))
            tmp = ''
        elif char == 'D':
            stack.append(pow(int(tmp), 2))
            tmp = ''
        elif char == 'T':
            stack.append(pow(int(tmp), 3))
            tmp = ''
        elif char == '*':
            num1 = stack.pop()
            if len(stack) == 0:
                stack.append(num1*2)
                continue
            num2 = stack.pop()
            stack.append(num2*2)
            stack.append(num1*2)
        elif char == '#':
            num = stack.pop()
            stack.append(num*-1)
        else:
            tmp += char
    print(stack)
    print(sum(stack))
    return sum(stack)

solution("1D2S#10S*")
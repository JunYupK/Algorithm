from collections import deque
def solution(order):
    answer = 0
    boxs = deque([i for i in range(1, len(order)+1)])
    stack = []
    for o in order:
        if boxs and stack:
            if boxs[0] > o:
                if stack[-1] == o:
                    stack.pop()
                    answer += 1
                else:
                    break
            elif boxs[0] <= o:
                tmp = 0
                while boxs:
                    tmp = boxs.popleft()
                    if tmp == o:
                        answer += 1
                        break
                    stack.append(tmp)
        elif boxs and len(stack) == 0:
            if boxs[0] > o:
                break
            elif boxs[0] <= o:
                tmp = 0
                while boxs:
                    tmp = boxs.popleft()
                    if tmp == o:
                        answer += 1
                        break
                    stack.append(tmp)
        elif len(boxs) == 0 and stack:
            if stack[-1] == o:
                stack.pop()
                answer += 1
            else:
                break
        else:
            break
    print(answer)
    return answer
solution([4, 3, 1, 2, 5])
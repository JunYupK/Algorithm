def solution(ingredient):
    answer = 0
    hamburger = [1,2,3,1]
    stack = []
    for num in ingredient:
        stack.append(num)
        if len(stack) >= 4:
            tmp = stack[-4:-1] + [stack[-1]]
            if tmp == hamburger:
                answer += 1
                for i in range(4):
                    stack.pop()
    return answer
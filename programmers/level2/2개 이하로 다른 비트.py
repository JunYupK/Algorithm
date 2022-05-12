def solution(numbers):
    answer = []
    for num in numbers:
        if num %2 ==0:
            answer.append(num+1)
        else:
            lastZero = (num+1) & (-num)
            zero_toOne = num | lastZero
            temp = (zero_toOne & (~(lastZero)>> 1))
            answer.append(temp)
    return answer

# 코드 출처 https://velog.io/@redcarrot01/ProblemSolving-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%9B%94%EA%B0%84%EC%BD%94%EB%93%9C%EC%B1%8C%EB%A6%B0%EC%A7%80-2%EA%B0%9C%EC%9D%B4%ED%95%98%EB%A1%9C%EB%8B%A4%EB%A5%B8%EB%B9%84%ED%8A%B8-Level2
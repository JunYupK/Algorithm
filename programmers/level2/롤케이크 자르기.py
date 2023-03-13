def solution(topping):
    answer = 0
    checkSum = set()
    dp1 = [0] * (len(topping)+1)
    dp2 = [0] * (len(topping) + 1)
    for i, topp in enumerate(topping):
        checkSum.add(topp)
        dp1[i] = len(checkSum)
    checkSum = set()
    for i in range(len(topping)-1, -1, -1):
        checkSum.add(topping[i])
        dp2[i] = len(checkSum)
    for i in range(len(dp1)-1):
        if dp1[i] == dp2[i+1]:
            answer += 1
    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])
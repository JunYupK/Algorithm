def solution(N):
    largest = 0
    shift = 0
    temp = N
    if temp == 0:
        return 1
    for i in range(1, 30):
        index = (temp & 1)
        temp = (temp >> 1) | (index << 29)
        if (temp > largest):
            largest = temp
            shift = i
    return shift


# print(solution(9736))
print(solution(0))
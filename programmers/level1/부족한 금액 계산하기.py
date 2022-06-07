def solution(price, money, count):
    answer = -1
    result = 0
    sum = 0
    for i in range(count):
        result += price
        sum += result
    if sum <= money:
        answer = 0
    else:
        answer = sum - money
    return answer

solution(3,20,4)
def count_divisor(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 2
    num = n//2 + 1
    count = 0
    for i in range(1, num):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = count_divisor(i)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

print(solution(1,2))
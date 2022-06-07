def solution(n):
    answer = 0
    result = ''
    i = 3
    while n != 0:
        result += str(n%i)
        n = n // i
    result = result[::-1]
    i = 1
    for char in result:
        answer += int(char) * i
        i *= 3
    return answer

solution(125)
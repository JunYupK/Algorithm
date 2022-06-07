def solution(n):
    return [int(i) for i in list(str(n))[::-1]]

n = 12345
print(solution(n))
def solution(s):
    s = [int(i) for i in s.split(' ')]
    answer = ''
    answer += str(min(s))
    answer += ' '
    answer += str(max(s))
    return answer

s = "-1 -2 -3 -4"
solution(s)
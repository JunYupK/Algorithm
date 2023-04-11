def solution(k, m, score):
    answer = 0
    q = []
    score.sort(reverse = True)
    for i in range(m-1, len(score), m):
        if i > len(score)-1:
            break
        answer += score[i] * m
    
    return answer
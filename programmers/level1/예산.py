def solution(d, budget):
    answer = 0
    result = 0
    d.sort()
    for n in d:
        result += n
        if result > budget:
            break
        answer += 1
    return answer
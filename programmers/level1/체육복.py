def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    lost = sorted(lost)
    reserve = sorted(reserve)
    tmp = lost[:]
    for l in tmp:
        if l in reserve:
            answer += 1
            lost.remove(l)
            reserve.remove(l)
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l + 1 in reserve:
            reserve.remove(l+1)
            answer += 1
    return answer

print(solution(5, [1,2,4], [2,3,4,5]))
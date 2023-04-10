def solution(sequence, k):
    answer = []
    left, right = 0, 0
    _sum = 0
    flag = True
    while right != len(sequence):
        if flag:
            _sum += sequence[right]
            
        if left == right:
            if _sum == k:
                answer.append([left,right])
            right += 1
            flag = True
            continue
        if k > _sum:
            right += 1
            flag = True
        elif k < _sum:
            _sum -= sequence[left]
            left += 1
            flag = False
        else:
            answer.append([left,right])
            right += 1
            flag = True
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    return answer[0]
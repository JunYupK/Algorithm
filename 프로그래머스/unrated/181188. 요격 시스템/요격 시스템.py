def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    flag = targets[0][1] - 0.1
    for i in range(1,len(targets)):
        if targets[i][0] < flag < targets[i][1]:
            continue
        else:
            answer += 1
            flag = targets[i][1] - 0.1
    return answer
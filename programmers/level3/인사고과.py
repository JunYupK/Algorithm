from collections import deque
def solution(scores):
    insentive = []
    q = deque(scores)
    target = scores[0]
    scores = scores[1:]
    scores.sort(key=lambda x:(x[0],x[1]), reverse= True)
    while scores:
        flag = False
        t_left, t_right = scores.pop()
        for left,right in scores:
            if t_left < left and t_left < right:
                flag = True
                break
        if flag:
            continue
        insentive.append([t_left,t_right])
    insentive.sort(key=lambda x:(x[0] + x[1]), reverse=True)
    print(insentive)
    answer = 1
    for left, right in insentive:
        if left > target[0] and right > target[1]:
            return -1
        if left + right <= sum(target):
            return answer+1
        answer += 1
    return answer + 1
print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
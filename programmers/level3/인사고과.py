def solution(scores):
    answer = 0
    target = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    for i in range(1, len(scores)):
        if scores[i][1] < scores[i-1][1]:
            if scores[i] == target:
                return -1
            scores[i][1] = -scores[i][1]
    scores.sort(key=lambda x:(x[0]+x[1]), reverse=True)
    for i, score in enumerate(scores):
        if sum(score) > sum(target):
            answer += 1
    return answer + 1
solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]])
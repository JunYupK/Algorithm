def solution(flowers):
    count = 0
    answer = [0]*366
    for start,end in flowers:
        answer[start] += 1
        answer[end] += -1
    for i in range(len(answer)-1):
        answer[i+1] += answer[i]
    for a in answer:
        if a > 0:
            count += 1
    return count

solution(
[[3, 4], [4, 5], [6, 7], [8, 10]])
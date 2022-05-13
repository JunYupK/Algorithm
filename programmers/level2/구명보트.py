from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people)
    q = deque(sorted(people))
    print(q)
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
            answer += 1
        elif q[0] <= limit:
            q.pop()
            answer += 1

    if len(q) == 1:
        answer += 1
    print(answer)
    return answer

people = [70, 80, 50]
limit = 100
solution(people, limit)

#한번 해볼까? 해서 짜서 넣어본 코드인데 효율성, 정확도도 통과해서 놀란 코드이다.
#일단 사람들의 무게만큼 sort 후에 가장 무거운 사람과 가벼운사람의 합이 보트 제한보다 낮으면 둘다 태우고 합이 limit보다 크면 앞의 사람을 태우는 식의 코드
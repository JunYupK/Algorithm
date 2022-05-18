def solution(answers):
    answer = []
    first = [1,2,3,4,5] * 2000
    second = [2,1,2,3,2,4,2,5]* 1800
    third = [3,3,1,1,2,2,4,4,5,5] * 1000
    human = {}
    human[1] = 0
    human[2] = 0
    human[3] = 0
    for i in range(len(answers)):
        if first[i] == answers[i]:
            human[1] += 1
        if second[i] == answers[i]:
            human[2] += 1
        if third[i] == answers[i]:
            human[3] += 1
    human = sorted(human.items() , key=lambda x:(x[1]), reverse = True)
    answer.append(human[0][0])
    print(human)
    for i in range(1 ,len(human)):
        if human[0][1] == human[i][1]:
            answer.append(human[i][0])
    print(answer)
    return answer

answers = [1,2,3,4,5]
solution(answers)
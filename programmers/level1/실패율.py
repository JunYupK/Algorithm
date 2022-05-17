def solution(N, stages):
    answer = []
    sol = []
    stages = sorted(stages)
    stageDict = {}
    for i in range(1, N+1):
        stageDict[i] = 0
    for stage in stages:
        if stageDict.get(stage) is None:
            break
        stageDict[stage] += 1
    total = len(stages)
    for i in range(1, N+1):
        tmp = stageDict[i]
        if total == 0:
            answer.append((0, i))
            continue
        answer.append((float(tmp/total), i))
        total -= tmp
    answer = sorted(answer, key=lambda x:x[0], reverse= True)
    for i, j in answer:
       sol.append(j)

    return sol

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(n, stages)
print(0/5)
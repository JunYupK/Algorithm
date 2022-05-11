from itertools import permutations
def solution(k, dungeons):
    answer = []
    for per in permutations(dungeons,len(dungeons)):
        count = 0
        fatigue = k
        for i in range(len(per)):
            if per[i][0] > fatigue or per[i][1] > fatigue:
                answer.append(count)
                break
            fatigue -= per[i][1]
            count += 1
            if i == len(per) - 1:
                answer.append(count)
    print(max(answer))
    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]
solution(k, dungeons)

#던전의 최대 갯수가 적어서 permutations 함수를 이용해 모든 던전의 경우의 수를 계산하여 풀었다.
# 입장피로도와 소모피로도 관계를 이용한 우선순위를 매겨서 정렬하는 방법도 있을 것 같다.
# + DFS를 활용도 가능하다
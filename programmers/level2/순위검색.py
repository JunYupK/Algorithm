from itertools import permutations,combinations
from collections import defaultdict
from bisect import bisect_left,bisect_right
def solution(info, query):
    answer = []
    candidates = []
    candi_dict = defaultdict(list)
    for i in range(1,5):
        candidates.extend(combinations(range(4),i))

    for data in info:
        data = data.split(" ")
        num = data[-1]
        del data[-1]
        tmp = data[:]
        candi_dict["".join(tmp)].append(int(num))
        for candi in candidates:
            for i in candi:
                tmp[i] = '-'
            tmp = "".join(tmp)
            candi_dict[tmp].append(int(num))
            tmp = data[:]
    for i in candi_dict.values():
        i.sort()

    for q in query:
        q = q.split(" and ")
        tmp = q[-1].split(" ")
        del q[-1]
        q.append(tmp[0])
        num = int(tmp[-1])

        num_list = candi_dict["".join(q)]
        count = len(num_list) - bisect_left(num_list, num)
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)

#2단계라고 믿기 어려울 정도로 어려운 문제였다;; combination을 이용한 인덱스로 다양한 조합의 str을 만드는 부분이 후보키 문제와 상당히 흡사했다.
#그리고 또한 lower_bound 를 이용하여 정렬된 리스트에서 특정 한 수 이상을 찾는 효율성 문제도 이진탐색을 고려한 문제였다
#python 라이브러리에는 이진탐색을 도와주는 bisect_left, right를 제공한다. 더불어 COUNTER 라이브러리도 알아 두도록 하자.
# 보통 효율성 문제에서는 딕셔너리나 이진탐색 중 하나는 떠올리기는 쉽지만 둘다 활요하는 경우도 있다는것을 생각하자
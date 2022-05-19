from collections import defaultdict
import sys
def solution(enroll, referral, seller, amount):
    node = defaultdict(list)
    income = {}
    for i, name in enumerate(referral):
        node[enroll[i]] = name
        income[enroll[i]] = 0
    for i, name in enumerate(seller):
        target = name
        tmp = amount[i] * 100
        while target != '-':
            fees = tmp // 10 #수수료
            tmp -= fees
            income[target] += tmp
            tmp = fees
            target = node[target]
            if fees == 0:
                break
    return list(income.values())
#처음엔 자식 노드가 없는 노드에만 집중을 해서 각 노드의 자식들을 딕셔너리로 체킹해두고 dfs로 합의 10% 씩 수수료를 먹이면서 돌아오는 방식을 채택했었는데 그러면 각각 판매의 수수료가 아니라
# 판매의 커미션의 합의 10% 가 되어서 다 틀렸었다.
# 그래서 반대로 부모 노드를 체킹해두고 수입이 있는 노드의 부모들을 타고 올라가면서 커미션을 주는 형식으로 하였으나 또 틀렸었다.
# 이유는 seller의 반복문 수를 줄이려고 각 노드가 판매한 칫솔의 총합의 커미션을 부모노드를 타고 가면서 주는 형식으로 짰으나, 각 칫솔의 판매마다 커미션을 주는 형식이므로
# 각 칫솔의 판매마다 커미션을 주는 형식으로 코드를 변경하니 한번에 통과하였다 ㅡ.ㅡ
# 그래프 문제이기는 하나 그래프가 아닌거같은 문제이다.
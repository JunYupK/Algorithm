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
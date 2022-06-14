from bisect import bisect_left, bisect_right
from collections import defaultdict
def solution(n, plans, clients):
    answer = []
    plan_dict = defaultdict(list)
    tmp = []
    for i ,p in enumerate(plans):
        p = p.split(' ')
        tmp += [int(i) for i in p[1:]]
        tmp.sort()
        tmp2 = tmp[:]
        plan_dict[int(p[0])] = tmp2
    key_list = list(plan_dict.keys())
    for c in clients:
        c = c.split(' ')
        data = int(c[0])
        service = [int(i) for i in c[1:]]
        i = bisect_left(key_list, data)
        service_check = False
        for j in range(i,len(key_list)):
            check = True
            tmp = plan_dict[key_list[j]]
            for s in service:
                num = bisect_left(tmp, s)
                if num >= len(tmp) or num < 0:
                    check = False
                    break
                elif tmp[num] != s:
                    check = False
                    break
            if check:
                answer.append(j+1)
                service_check = True
                break
        if service_check is False:
            answer.append(0)
    print(answer)
    return answer

n = 5
plans = ["100 1 3", "500 4", "2000 5"]
clients = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]
solution(n, plans, clients)

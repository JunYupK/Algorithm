def solution(p):
    answer = []
    num_dic = {}
    for num in range(len(p)):
        num_dic[num] = 0
    i = 0
    count = 0
    while i != len(p):
        j = p.index(min(p[i:]))
        if p[i] != p[j]:
            tmp = p[i]
            p[i] = p[j]
            p[j] = tmp
            num_dic[i] += 1
            num_dic[j] += 1
        i += 1
    return list(num_dic.values())

p = [2, 5, 3, 1,4]
solution(p)
def solution(name, yearning, photo):
    answer = []
    human_dict = {}
    for i in range(len(name)):
        human_dict[name[i]] = yearning[i]
    for p in photo:
        tmp = 0
        for x in p:
            if x in human_dict:
                tmp += human_dict[x]
        answer.append(tmp)
    return answer
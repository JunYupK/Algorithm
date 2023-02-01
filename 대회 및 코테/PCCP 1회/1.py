def solution(input_string):
    answer = []
    alpha_count ={}
    result = list(input_string)
    for i in range(1, len(result)):
        if result[i-1] == result[i]:
            result[i-1] = '*'
    result = "".join(result).replace('*','')
    for s in result:
        if s in alpha_count.keys():
            alpha_count[s] += 1
        else:
            alpha_count[s] = 1

    for k,v in alpha_count.items():
        if v > 1:
            answer.append(k)
    answer.sort()
    answer = "".join(answer)
    if len(answer) == 0:
        return "N"
    else:
        return answer
solution('edeaaabbccd')
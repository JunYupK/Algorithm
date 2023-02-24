def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for char in target:
            flag = True
            _min = 1e9
            for keys in keymap:
                if _min > keys.find(char) + 1 and keys.find(char) != -1:
                    _min = keys.find(char) + 1
            if _min == 1e9:
                flag = False
                break
            result += _min
        if flag:
            answer.append(result)
        else:
            answer.append(-1)
    print(answer)

    return answer

solution(["AA"], ["B"])

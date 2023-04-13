def solution(babbling):
    answer = 0
    pron_dict = {"aya":1, "ye":1, "woo":1, "ma":1}
    for babble in babbling:
        tmp = ''
        stack = []
        for char in babble:
            tmp += char
            if len(tmp) > 3:
                stack = []
                break
            else:
                if tmp in pron_dict:
                    if stack and stack[-1] != tmp:
                        stack.append(tmp)
                        tmp = ''
                    elif len(stack) == 0:
                        stack.append(tmp)
                        tmp = ''
                    elif stack and stack[-1] == tmp:
                        stack = []
                        tmp = ''
                        break
        if tmp:
            if tmp not in pron_dict:
                stack = []
            else:
                if stack and stack[-1] == tmp:
                    stack = []
                else:
                    stack.append(tmp)
        if stack:
            answer += 1
    return answer
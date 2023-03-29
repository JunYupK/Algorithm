from collections import Counter


def solution(s, skip, index):
    answer = ''
    alpha_dict = Counter(skip)
    for i in range(len(s)):
        count = index
        tmp = ord(s[i])
        while count != 0:
            tmp = tmp + 1
            if tmp > 122:
                tmp = 97
            if chr(tmp) not in alpha_dict:
                count -= 1
        answer += chr(tmp)
    return answer
solution("aukks", "wbqd", 5)
def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        for i ,char in enumerate(word):
            if i % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        answer += ' '
    print(answer[:-1])

    return answer[:-1]

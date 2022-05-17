def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for s in new_id:
        if s.isalnum() or s in '-_.':
            answer += s
    while '..' in answer:
        answer = answer.replace('..','.')
    answer = answer.strip('.')
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[14] == '.':
            answer = answer[0:14]
    if len(answer) <= 2:
        tmp = answer[-1]
        while len(answer) != 3:
            answer += tmp
    return answer

new_id = "abcdefghijklmn.p"
solution(new_id)
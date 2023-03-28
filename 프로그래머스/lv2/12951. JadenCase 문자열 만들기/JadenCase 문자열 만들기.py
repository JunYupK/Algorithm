def solution(s):
    answer = ''
    str_arr = s.split(' ')
    for index, string in enumerate(str_arr):
        for i, char in enumerate(string):
            if i == 0 and char.isalpha():
                answer += char.upper()
            else:
                if char.isalpha():
                    answer += char.lower()
                else:
                    answer += char
        if index < len(str_arr)-1:
            answer += ' '
    return answer
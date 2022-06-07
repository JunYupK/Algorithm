def solution(s, n):
    answer = ''
    for char in s:
        if 65 <= ord(char) <= 90:
            tmp = ord(char) + n
            if tmp > 90:
                tmp = tmp % 90
                tmp = tmp + 64
            answer += chr(tmp)
        elif 97 <= ord(char) <= 122:
            tmp = ord(char) + n
            if tmp > 122:
                tmp = tmp % 122
                tmp = tmp + 96
            answer += chr(tmp)
        else:
            answer += char
    return answer

print(solution('z', 1))
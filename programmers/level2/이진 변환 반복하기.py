def solution(s):
    count = 0
    x = 0
    while s != '1':
        count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s)).replace('0b','')
        x += 1
    return [x, count]

s = "110010101001"
solution(s)
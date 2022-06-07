def solution(s):
    n = len(s)
    if n % 2 == 0:
        i = n//2
        return s[i-1:i+1]
    else:
        i = n//2
        return s[i]

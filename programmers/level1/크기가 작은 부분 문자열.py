def solution(t, p):
    answer = 0
    arr = []
    n, inc = len(t), len(p)
    for i in range(n-inc+1):
        arr.append(int(t[i:i+inc]))
    for num in arr:
        if num <= int(p):
            answer += 1
    return answer
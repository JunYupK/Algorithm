from collections import  deque
def solution(arr):
    q = deque()
    for n in arr:
        if len(q) != 0 and q[-1] == n:
            continue
        else:
            q.append(n)
    print(q)
    return list(q)

answer = [1,1,3,3,0,1,1]
solution(answer)
from collections import deque
def solution(n, lighthouse):
    answer = 0
    edges = [0] * (n+1)
    lines = []
    for start, end in lighthouse:
        lines.append([start,end])
        lines.append([end,start])
        edges[start] += 1
        edges[end] += 1
    q = deque()
    for i in range(1, len(edges)):
        if edges[i] == 1:
            edges[i] -= 1
            q.append((i, 1))
    while q:
        print(q)
        data, depth = q.popleft()
        for a, b in lines:
            if a == data:
                edges[b] -= 1
        for i in range(1,len(edges)):
            if edges[i] == 1:
                edges[i] -= 1
                q.append((i, depth+1))
    return answer
solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]])
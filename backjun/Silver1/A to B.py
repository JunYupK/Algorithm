from collections import deque

A, B = map(int,input().split())

def bfs(A, B):
    visited = {}
    visited[A] = True
    q = deque()
    q.append((A, 0))
    while q:
        num, count = q.popleft()
        if num == B:
            return count + 1
        case1 = num * 10 + 1
        case2 = num * 2
        if case1 not in visited and case1 <= B:
            visited[case1] = True
            q.append((case1 , count+1))
        if case2 not in visited and case2 <=B:
            visited[case2] = True
            q.append((case2, count + 1))

result = bfs(A,B)
if result is None:
    print(-1)
else:
    print(result)
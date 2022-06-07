from collections import deque
def BFS(edges, start, visited):
    q = deque()
    visited[start] = True
    q.append(start)
    count = 1
    while q:
        data = q.popleft()
        for left, right in edges:
            if left == data:
                if visited[right] is False:
                    visited[right] = True
                    q.append(right)
                    count += 1
            elif right == data:
                if visited[left] is False:
                    visited[left] = True
                    q.append(left)
                    count += 1
    return count
def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        visited = [False] * (n + 1)
        tmp = wires[:]
        del wires[i]
        num = BFS(wires,wires[0][0], visited)
        wires = tmp[:]
        answer.append(abs((n-num) - num))
    return min(answer)

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n,wires)
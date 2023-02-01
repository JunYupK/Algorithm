from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = []
    board = [['.'] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    moves = [[1,0, 'd'],[0,-1,'l'],[0,1,'r'], [-1,0, 'u']]
    q = deque()
    q.append(('', x-1, y-1, k))
    while q:
        route, pos_x, pos_y, count = q.popleft()
        if count<0:
            break
        if count == 0 and pos_x == r-1 and pos_y == c-1:
            answer.append(route)
            break
        for dx, dy, name in moves:
            next_x, next_y = pos_x + dx, pos_y + dy
            if 0 <= next_x < n and 0 <= next_y < m:
                if visited[next_x][next_y] is False or visited[next_x][next_y] != count:
                    q.append((route + name, next_x, next_y, count - 1))
                    visited[next_x][next_y] = count
    if len(answer) == 0:
        return "impossible"
    return answer[0]
solution(3, 3, 1, 2, 3, 3, 4)


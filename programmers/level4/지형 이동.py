from collections import deque
import heapq
def solution(land, height):
    answer = 0
    n = len(land)
    board = [[-1] * (n) for _ in range(n)]
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = land[i][j]
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]
    q = []
    q.append((0,0,0))
    visited[0][0] = 0
    count = 0
    ladder = 0
    while q:
        cost , x, y = heapq.heappop(q)
        if visited[x][y] == True:
            continue
        visited[x][y] = True
        ladder += cost
        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
            if abs(board[dx][dy] - board[x][y]) <= height:
                value = 0
            else: #사다리 설치
                value = abs(board[dx][dy] - board[x][y])

            if visited[dx][dy] is False: #방문하지 않은곳이라면
                heapq.heappush(q, (value, dx, dy))
                count += 1

    print(ladder)
    return ladder

# land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
solution(land,3)


#heapq 를 활용한 bfs 아이디어 문제이다. DFS와 비슷한 느낌으로 구역을 나누어서 탐색하는 느낌이다. 이동하는곳과의 value차이라거나 bfs를 할때
#조건부로 다음 이동장소를 정하는 아이디어는 기억해두면 좋을 것 같다.
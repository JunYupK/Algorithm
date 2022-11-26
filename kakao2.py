from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = []
    results = []
    board = [["X"] * (m + 2) for _ in range(n+2)]
    visited = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            board[i+1][j+1] = "."
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    updown = ["u", "d", "l", "r"]
    board[x][y] = "S"
    board[r][c] = "E"
    q = deque([(x, y, "", 0)])
    visited[x][y] == 1
    while q:
        i, j, result, count = q.popleft()
        if board[i][j] == "E":
            results.append("".join(result))
        for u in range(4):
            nextX, nextY = i+dx[u], j+dy[u]
            if count >= k:
                break
            if board[nextX][nextY] == "E":
                results.append(result + updown[u])
            if board[nextX][nextY] == "X":
                continue
            else:
                q.append([nextX, nextY, result + updown[u], count + 1])
    print(results)
    results.sort()
    if len(results) == 0:
        return "impossible"
    for result in results:
        if len(result) == k:
            return result
    return "impossible"
solution(3,3,1,2,3,3,4)

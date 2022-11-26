from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = []
    board = [["X"] * (m + 2) for _ in range(n+2)]
    visitied = [[0]*(m+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            board[i+1][j+1] = "."
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    updown = ["u", "d", "l", "r"]
    board[x][y] = "S"
    board[r][c] = "E"
    q = deque([(x, y, "", 0)])
    visitied[x][y] += 1
    while q:
        i, j, result, count = q.popleft()
        if count == k and board[i][j] == "E":
            answer.append("".join(result))
        for u in range(4):
            nextX, nextY = i+dx[u], j+dy[u]
            if count >= k:
                continue
            elif board[nextX][nextY] == "X":
                continue
            elif len(result) != 0 and result[-1] == "u" and updown[u] == "d" and board[nextX][nextY] != "E" and board[i][j] != "E":
                continue
            elif len(result) != 0 and result[-1] == "d" and updown[u] == "u" and board[nextX][nextY] != "E" and board[i][j] != "E":
                continue
            elif len(result) != 0 and result[-1] == "l" and updown[u] == 'r' and board[nextX][nextY] != "E" and board[i][j] != "E":
                continue
            elif len(result) != 0 and result[-1] == "r" and updown[u] == "l" and board[nextX][nextY] != "E" and board[i][j] != "E":
                continue
            else:
                visitied[nextX][nextY] += 1
                q.append([nextX, nextY, result + updown[u], count + 1])
    answer.sort()
    if len(answer) == 0:
        return "impossible"
    return answer[0]
solution(3,4,2,3,3,1,5)

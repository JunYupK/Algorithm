햣 from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1]* (n+2) for _ in range(n+2)]
    visited = [[[1e9]* (n+2) for _ in range(n+2)] for _ in range(4)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    #상 0, 하 1, 좌 2 우 3
    move_x = [-1, 1 ,0 , 0]
    move_y = [0, 0,-1,1]
    q = deque()
    q.append([1,1,0,1])
    visited[1][1] = 0
    new_board[1][1] = 1

    while q:
        x, y, cost, direction = q.popleft()
        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if new_board[dx][dy] == 0:
                if x == 1 and y == 1:
                    value = cost + 100
                else:
                    if direction == i:
                        value = cost + 100
                    else:
                        value = cost + 600

                if visited[i][dx][dy] == False:
                    visited[i][dx][dy] = value
                    q.append([dx,dy,value,i])
                else:
                    if visited[i][dx][dy] >= value:
                        visited[i][dx][dy] = value
                        q.append([dx,dy,value,i])
    min_value = visited[0][n][n]
    for i in range(4):
        if min_value >= visited[i][n][n]:
            min_value = visited[i][n][n]
    return min_value

board = 	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
solution(board)

# 방향을 고려하는 bfs 문제이지만 마지막 최근에 추가된 25번 케이스의 경우 마지막에 도착하는 방향까지 고려를 해야하는 문제여서 3차원 배열을 사용하였다.
# 3차원 배열을 처음 사용하는 문제이니 만큼 아마 당시 문제를 처음 푸는 과정에서는 25번케이스까지는 고려가 안되어서 3단계 문제였던거 같다.
#만약 마지막 방향까지 고려를 해야한다는 것을 알면 level 은 더 높아질꺼라 생각한다.

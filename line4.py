from collections import deque
def solution(grid, k):
    answer = -1
    q = deque()
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    visited[0][0] = True
    q.append([0, 0, 0, 0])
    n = len(grid) - 1
    m = len(grid[0]) -1
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x, y, count, day= q.popleft()
        print(x,y)
        answer = day
        #백트랙킹
        for i in range(4):
            x_next = dx[i] + x
            y_next = dy[i] + y
            if x_next >= len(grid) or x_next < 0 or y_next < 0 or y_next >= len(grid[0]):
                continue
            #이동후에 야영을 해야한다면 평지로만 이동이 가능
            if count + 1 == k:
                if grid[x_next][y_next] == '.' and visited[x_next][y_next] is False:
                    visited[x_next][y_next] = day + 1
                    q.append([x_next,y_next,0, day + 1])
            if grid[x_next][y_next] != '#':
                if grid[x_next][y_next] == '.':
                    visited= day + 1
                    q.append([x_next,y_next,0,day + 1])

grid = ["..FF", "###F", "###."]
print(solution(grid, 4))



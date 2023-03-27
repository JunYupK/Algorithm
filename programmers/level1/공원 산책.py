def solution(park, routes):
    answer = []
    moves = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
    pos_x, pos_y = 0, 0
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                pos_x, pos_y = i, j
                break
    for route in routes:
        direction, count = route.split(' ')
        next_x, next_y = pos_x, pos_y
        flag = True
        for i in range(int(count)):
            next_x += moves[direction][0]
            next_y += moves[direction][1]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                flag = False
                break
            elif 0 <= next_x < n and 0 <= next_y < m:
                if park[next_x][next_y] == 'X':
                    flag = False
                    break
        if flag is True:
            pos_x, pos_y = next_x, next_y

    return [pos_x, pos_y]
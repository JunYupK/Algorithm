# x 가 더 많을 경우
# o 가 1개 이상 더 많을 경우
# 둘 다 이긴 경우
# o 가 이겼지만 o 가 1개 더 많지 않을 경우
# x 가 이기고 o 와 x 개수가 같지 않을 경우
def solution(board):
    answer = -1
    o_count, x_count = 0,0
    o_win, x_win = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            elif board[i][j] == 'X':
                x_count += 1
    if o_count + x_count == 0:
        return 1
    if o_count - x_count > 1:
        return 0
    if x_count > o_count:
        return 0
    #행렬검사
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                o_win += 1
            elif board[i][0] == 'X':
                x_win += 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                o_win += 1
            elif board[0][i] == 'X':
                x_win += 1
    #대각 검사
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            o_win += 1
        elif board[0][0] == 'X':
            x_win += 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            o_win += 1
        elif board[0][2] == 'X':
            x_win += 1
    
    if o_win == x_win and o_win == 0:
        return 1
    if x_win == 0 and o_win > 0:
        if o_count > x_count:
            return 1
    if x_win > 0 and o_win == 0:
        if x_count == o_count:
            return 1
    return 0
    return answer
# O랑 X 둘다 승리조건을 갖춘 경우 불가능
# X가 O보다 많은 경우 불가능
# O가 X보다 2개이상 많은경우 불가능
# O가 승리했는데 X와 O의 개수가 같은경우
# X가 승리했는데 O가 하나 더 많은경우
def solution(board):
    answer = -1
    o_count, x_count = 0,0
    o_win, x_win = 0,0
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
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            elif board[i][j] == 'X':
                x_count += 1
    check = o_count - x_count
    if check < 0:
        return 0
    elif check > 1:
        return 0
    elif o_win + x_win > 1:
        return 0
    elif o_win == 1 and check != 1:
        return 0
    elif x_win == 1 and check != 0:
        return 0
    return 1
print(solution(["XO.", "OXO", "XOX"]))
# ["XXX", "...", "OOO"]

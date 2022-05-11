def solution(m, n, board):
    answer = 0
    new_board = []
    for i in board:
        new_board.append(list(i))
    tmp = [[False] * n for _ in range(m)]
    for i in range(m):
        if i == len(board) - 1:
            continue
        for j in range(n):
            if j == len(board[i]) -  1:
                continue
            if new_board[i][j] == '':
                continue
            if new_board[i][j] == new_board[i+1][j] and new_board[i][j] == new_board[i+1][j+1] and new_board[i][j] == new_board[i][j+1]:
                new_board[i][j] = ''
                new_board[i][j+1] = ''
                new_board[i+1][j] = ''
                new_board[i+1][j+1] = ''
    for data in new_board:
        print(data)
    print()
    #내리기
    for i in range(m):
        if i == len(board) - 1:
            continue
        for j in range(n):
            if new_board[i][j] == '':
                continue
            else:
                if new_board[i+1][j] == '':
                    new_board[i+1][j] = new_board[i][j]
                    new_board[i][j] = ''


    for data in new_board:
        print(data)
    return answer

board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
tmp = []
m = 6
n = 6
solution(m,n,board)

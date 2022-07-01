# n ,m, r = map(int,input().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int,input().split())))
#
# for _ in range(r):
#     if min(n ,m) <= 2:
#         # 왼쪽아래에 둘 숫자 저장
#         num = board[n - 1][0]
#         # 외부 왼쪽
#         for j in range(n - 2, -1, -1):
#             board[j + 1][0] = board[j][0]
#         # 외부 위
#         for j in range(1, m):
#             board[0][j - 1] = board[0][j]
#         # 외부 오른쪽
#         for j in range(1, n):
#             board[j - 1][m - 1] = board[j][m - 1]
#         # 외부 아래
#         for j in range(m - 2, 0, -1):
#             board[n - 1][j + 1] = board[n - 1][j]
#         board[n - 1][1] = num
#
#     else:
#         for
#         # 왼쪽아래에 둘 숫자 저장
#         num = board[n - 1][0]
#         # 외부 왼쪽
#         for j in range(n - 2, -1, -1):
#             board[j + 1][0] = board[j][0]
#         # 외부 위
#         for j in range(1, m):
#             board[0][j - 1] = board[0][j]
#         # 외부 오른쪽
#         for j in range(1, n):
#             board[j - 1][m - 1] = board[j][m - 1]
#         # 외부 아래
#         for j in range(m - 2, 0, -1):
#             board[n - 1][j + 1] = board[n - 1][j]
#         board[n - 1][1] = num
#
# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end=' ')
#     print()
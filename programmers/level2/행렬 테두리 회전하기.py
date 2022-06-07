def rotate_matrix(matrix,i1,j1,i2, j2):
    n = abs(i2 - i1) + 1
    m = abs(j2 - j1) + 1
    num = matrix[i1][j1]
    min_num = []
    #좌
    for i in range(i1+1, i1+n):
        matrix[i-1][j1] = matrix[i][j1]
        min_num.append(matrix[i][j1])
    #하
    for i in range(j1+1,j1+m):
        matrix[i2][i-1] = matrix[i2][i]
        min_num.append(matrix[i2][i])

    #우
    for i in range(i2-1,i1-1, -1):
        matrix[i+1][j2] = matrix[i][j2]
        min_num.append(matrix[i][j2])
    #상
    for i in range(j2-1,j1, -1):
        matrix[i1][i+1] = matrix[i1][i]
        min_num.append(matrix[i1][i])
    matrix[i1][j1+1] = num
    min_num.append(num)
    return matrix, min(min_num)
def solution(rows, columns, queries):
    answer = []
    cnt = 1
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt
            cnt += 1

    for i1,j1,i2,j2 in queries:
        matrix, tmp = rotate_matrix(matrix, i1-1,j1-1,i2-1,j2-1)
        answer.append(tmp)
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])

def make_binary(num, n):
    tmp = bin(num)
    tmp = tmp.replace('0b','')
    tmp = tmp.split()
    char = '0' * (n - len(tmp[0]))
    tmp.insert(0,char)
    return ''.join(tmp)
def solution(n, arr1, arr2):
    board1 = []
    board2 = []
    answer = []
    for i in range(n):
        num1, num2 = make_binary(arr1[i], n), make_binary(arr2[i], n)
        tmp1, tmp2 = '',''
        for j in range(n):
            if num1[j] == '1':
                tmp1 += '#'
            else:
                tmp1 += ' '
            if num2[j] == '1':
                tmp2 += '#'
            else:
                tmp2 += ' '
        board1.append(tmp1)
        board2.append(tmp2)

    for i in range(n):
        tmp = ''
        for j in range(n):
            if board1[i][j] == '#' or board2[i][j] == '#':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer

arr1 = [9,20,28,18,11]
arr2 = [30, 1, 21, 17, 28]
solution(5, arr1, arr2)

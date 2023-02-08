def division_search(left, right, arr):
    global flag
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    if arr[mid] == '0':
        for i in range(left, mid):
            if arr[i] == '1':
                flag = False
                return
        for i in range(mid + 1, right + 1):
            if arr[i] == '1':
                flag = False
                return
    division_search(left, mid - 1, arr)
    division_search(mid + 1, right, arr)


def solution(numbers):
    global flag
    answer = []
    for n in numbers:
        flag = True
        n = bin(n).replace('0b', '')
        index = 1
        node_count = 0
        while 1:
            if pow(2, index) - 1 >= len(n):
                node_count = pow(2, index) - 1
                break
            index += 1
        n = list(('0' * (node_count - len(n))) + n)
        division_search(0, len(n) - 1, n)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

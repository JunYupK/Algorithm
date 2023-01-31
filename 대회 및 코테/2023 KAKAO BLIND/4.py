global flag

def division_search(left, right, arr, prev_root):
    global flag
    if left >= right:
        return
    mid = (left + right) // 2
    print(mid)
    if arr[mid] == '0':
        if arr[mid-1] == '1' or arr[mid+1] == '1':
            flag = False
    division_search(left, mid-1,arr, arr[mid])
    division_search(mid + 1, right, arr, arr[mid])

def solution(numbers):
    global flag
    answer = []
    for n in numbers:
        flag = True
        n = bin(n).replace('0b','')
        index = 1
        node_count = 0
        while 1:
            if pow(2,index) - 1 >= len(n):
                node_count = pow(2,index) - 1
                break
            index += 1
        n = list(('0' * (node_count - len(n))) + n)
        print(n)
        if n[(len(n)-1)//2] != '0':
            division_search(0, len(n)-1, n, n[(len(n)-1)//2])
        else:
            flag = False
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer
solution([58])

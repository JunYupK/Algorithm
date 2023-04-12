import sys
input = sys.stdin.readline
def check_arr(a,b):
    b = b * 2
    for i in range(len(b)):
        count = 0
        for j in range(len(a)):
            if j+i >= len(b):
                return False
            if a[j] == b[j+i]:
                count += 1
            else:
                break
        if count == len(a):
            return True
    return False
N = int(input())
target = list(map(int,input().split()))
M = int(input())
direct = {1:3, 2:4, 3:1, 4:2}
answer = []
for _ in range(M):
    arr = list(map(int,input().split()))
    arr2 = []
    flag1 = check_arr(target,arr)
    for i in range(len(arr)):
        arr2.append(direct[arr[i]])
    arr2.reverse()
    flag2 = check_arr(target, arr2)
    if flag1 is True or flag2 is True:
        answer.append(arr)

print(len(answer))
for a in answer:
    print(*a)

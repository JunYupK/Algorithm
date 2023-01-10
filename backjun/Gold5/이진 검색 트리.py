import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
answer = []
def findTree(left, right):
    if left > right:
        return
    mid = right + 1
    answer.append(arr[left])
    for i in range(left + 1 ,right+1):
        if arr[i] > arr[left]:
            mid = i
            break
    findTree(left+1, mid - 1)
    findTree(mid, right)
    print(arr[left])

findTree(0,len(arr)-1)

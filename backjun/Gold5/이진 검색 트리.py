import sys
input = sys.stdin.readline
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
answer = []
def findTree(left, right):
    if left > right or right >= len(arr):
        return

    for i in range(right+1, len(arr)):
        if arr[right] > arr[i]:


findTree(0,0)
print(answer)
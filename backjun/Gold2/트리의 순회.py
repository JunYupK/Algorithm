import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorderPosition = [0] * (n+1)
for i in range(n):
    inorderPosition[inorder[i]] = i

def findPreOrder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    root = postorder[postEnd]
    print(root, end=" ")
    leftCount = inorderPosition[root] - inStart
    rightCount = inEnd - inorderPosition[root]
    findPreOrder(inStart, inStart + leftCount - 1 , postStart, postStart + leftCount - 1)
    findPreOrder(inEnd - rightCount + 1, inEnd, postEnd - rightCount, postEnd-1)
findPreOrder(0,n-1,0,n-1)
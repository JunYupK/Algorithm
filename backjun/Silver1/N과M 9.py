import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = []
check = [False] * N
def backtracking(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(0, N):
        if check[i] is False:
            ans.append(arr[i])
            check[i] = True
        else:
            continue
        backtracking(depth + 1, i+1, n, m)
        ans.pop()
        check[i]= False
backtracking(0,0,N,M)

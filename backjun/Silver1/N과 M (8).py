N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
ans = []
def backtracking(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(idx, n):
        ans.append(arr[i])
        backtracking(depth+1, i, n, m)
        ans.pop()
backtracking(0,0,N,M)
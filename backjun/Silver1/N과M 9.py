import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = set()
tmp = []
check = [False] * N
def backtracking(depth, idx, n, m):
    if len(tmp) == m:
        ans.add(tuple(tmp))
        return
    for i in range(n):
        if check[i] is True:
            continue
        tmp.append(arr[i])
        check[i] = True
        backtracking(depth + 1, i,n,m)
        check[i] = False
        tmp.pop()

backtracking(0,0,N,M)
for i in sorted(ans):
    print(*i)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp, ans = [], set()
def backtracking(depth, idx):
    if depth == M:
        ans.add(tuple(tmp))
        return
    for i in range(idx, N):
        tmp.append(arr[i])
        backtracking(depth+1, i)
        tmp.pop()

backtracking(0,0)
for i in sorted(ans):
    print(*i)

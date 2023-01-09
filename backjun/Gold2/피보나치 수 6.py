import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
p=1000000007

# for i in range(2, len(dp)):
#     dp[i] = dp[i-1] + dp[i-2]
# def fibonacci(x):
#     if x <= 1000000:
#         return dp[x]
#     return fibonacci(x-1) + fibonacci(x-2)
# print(fibonacci(n) % 1000000007)
#
# def fibonacci(x):
#     if x <= 1:
#         return x
#     return fibonacci(x-1) + fibonacci(x-2)
#
# print(fibonacci(n))
def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%p
    return temp
def power(adj,n):
    if n==1:
        return adj
    elif n%2:
        return multi(power(adj,n-1),adj)
    else:
        return power(multi(adj,adj),n//2)
adj=[[1,1],[1,0]]
#피보나치 초기값
start=[[1],[1]]
n=int(input())
if n<3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])
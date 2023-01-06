import sys
input = sys.stdin.readline
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
N, M = map(int, input().split())
answer = factorial(N) // (factorial(N-M) * factorial(M))
print(answer)
import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())
def recursion(a, b):
    if b == 1:
        return a % C
    tmp = recursion(a, b//2)
    if b % 2 == 0:
        return tmp * tmp % C
    else:
        return tmp * tmp * a % C

print(recursion(A,B))
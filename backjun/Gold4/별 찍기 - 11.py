import sys
input = sys.stdin.readline
n = int(input())

def print_tri(n):
    if n == 0:
        return
    space = (n-1) * ' '
    print(space + '*')
    space = (n-2) * ' '
    print(space + '* *')
    space = (n-3) * ' '
    print(space + '*****')
    print_tri(n-3)
print_tri(n)


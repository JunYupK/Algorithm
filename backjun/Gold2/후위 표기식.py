import sys
from collections import deque
input = sys.stdin.readline
data = list(input())
res = ''
stack = []
for s in data:
    if s.isalpha():
        res += s
    elif s == '(':
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()

while stack:
    res += stack.pop()
print(res)
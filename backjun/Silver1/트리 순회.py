import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = {}
for _ in range(n):
    node, left, right = map(str, input().split())
    graph[node] = [left, right]

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(graph[node][0])
        preorder(graph[node][1])
def midorder(node):
    if node != '.':
        midorder(graph[node][0])
        print(node, end='')
        midorder(graph[node][1])
def postorder(node):
    if node != '.':
        postorder(graph[node][0])
        postorder(graph[node][1])
        print(node, end='')
preorder('A')
print()
midorder('A')
print()
postorder('A')
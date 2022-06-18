from collections import deque
import sys
def inputD(num):
    return (num*2) % 10000
def inputS(num):
    if num == 0:
        num = 10000
    return num - 1
def inputL(num):
    return (10*num+(num//1000))%10000
def inputR(num):
    return (num//10+(num%10)*1000)%10000
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    register = ['D', 'S', 'L', 'R']
    visited = [False] * 10000
    q = deque()
    q.append(['first', A])
    while q:
        result, number = q.popleft()
        if result == 'first':
            result = ""
        if number == B:
            print(result)
            break
        for i in range(4):
            if register[i] == 'D':
                tmp = inputD(number)
            elif register[i] == 'S':
                tmp = inputS(number)
            elif register[i] == 'L':
                tmp = inputL(number)
            else:
                tmp = inputR(number)

            if visited[tmp] is False:
                visited[tmp] = True
                q.append([result+register[i], tmp])
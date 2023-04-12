import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    arr.append(set(tmp[1:]))
M = int(input())
students = []

for _ in range(M):
    tmp = list(map(int,input().split()))
    students.append(set(tmp[1:]))

for student in students:
    count = 0
    for a in arr:
        if student.intersection(a) == a:
            count += 1
    print(count)


from sys import stdin
from collections import deque
n, m = map(int,stdin.readline().split())
know_people = set(stdin.readline().split()[1:])
party = []
result = 0
for _ in range(m):
    party.append(set(input().split()[1:]))
for _ in range(m):
    for p in party:
        if p & know_people:
            know_people = know_people.union(p)

for p in party:
    if p & know_people:
        continue
    result += 1

print(result)
#왜 알고리즘문제에 파이썬이 엄청난지 알려주는 문제라고 생각한다.
# union, find 함수를 직접만들고 적용하는것도 좋은 공부겠지만, 파이썬에선 자체적으로 set 자료구조에서 add, union, 교집합 여부를 모두 지원해버리는걸 깜빡하고
# 함수를 정의하고 어떤식으로 집합을 묶는 고민을 하느라 시간을 썼는데 그냥 & 기호 하나로 교집합 여부를 체크해버리니 좀 허탈하기도 할 정도였다.
# 물론 근본적인 이론을 아는건 중요하지만 set 활용법을 더 알면 쉽게푸는 문제라고 생각한다.
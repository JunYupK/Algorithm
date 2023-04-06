from collections import deque
data = input()
answer = ''
q = deque()
for char in data:
    if q and q[0] != '<':
        if char == ' ':
            while q:
                answer += q.pop()
            answer += ' '
            continue
        elif char == '<':
            while q:
                answer += q.pop()
    elif q and q[0] == '<':
        if char == '>':
            while q:
                answer += q.popleft()
            answer += '>'
            continue
    q.append(char)
if q:
    while q:
        answer += q.pop()
print(answer)

from collections import deque
t = int(input())
for _ in range(t):
    order = input()
    n = int(input())
    data = input()

    if 'D' in order and n == 0:
        print("error")
        continue
    q = deque()
    if n > 0:
        data = data.strip('[]')
        data = data.split(',')
        for d in data:
            q.append(int(d))
    r_check = False
    check = False
    for char in order:
        if char == 'R':
            if r_check is False:
                r_check = True
            else:
                r_check = False
        elif char == 'D':
            if len(q) == 0:
                check = True
                break
            else:
                if r_check is True:
                    q.pop()
                else:
                    q.popleft()

    if check is True:
        print('error')
    else:
        if r_check is True:
            q = list(q)[::-1]
            print(str(q).replace(' ',''))
        else:
            q = list(q)
            print(str(q).replace(' ',''))
# 뭔 입력 형식과 출력형식까지 일일이 지정해줘야하는 매~우 불친절하고 귀찮은 문제이다. 문제 자체는 단순한 구현과 reverse의 효율성만 생각하면 되는 문제 퉤!
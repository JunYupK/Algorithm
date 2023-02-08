table = []
for i in range(10):
    temp = list(input())
    for j in range(10):
        if temp[j] == 'O':
            temp[j] = True #True: 불 켜져있음
            continue
        temp[j] = False #False: 불 꺼져있음
    table.append(temp)

# 5방탐색.
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 101
# 1열을 누르는 경우의 수 101010101010조사.
for f in range(1<<10):
    a = []
    for i in range(10):
        a.append(table[i][:])
    cnt = 0
    # 1행 10칸을 확인.(1행에서 스위치를 누른경우의 수를 모두 탐색.ㄴ
    for i in range(10):
        if f & (1<<i): #i번째 스위치를 누른 경우(눌려있는 경우)
            cnt += 1
            # 1행은 y좌표가 0이기때문에.
            for k in range(5):
                nx = i + dx[k]
                ny = 0 + dy[k]
                # True -> False , False-> True
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]

    # 1행은 위에 먼저 끝냈고 2행부터는 위쪽에 전등이 켜져있다면 스위치를 눌러주는식으로 진행한다.(무조건 위쪽만 본다.)
    for i in range(1, 10): #y좌표
        for j in range(10): #x좌표
            if not a[i-1][j]: #바로 윗 전등이 켜져있다면 스위치를 눌러줘야됨
                continue
            for k in range(5):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]
            cnt += 1
    # 다 끝났는데 마지막열에 켜져있으면 실패.
    can = True
    for i in range(10):
        if a[9][i] == True:
            can = False
    # 가능하면? ans에 최소값을 등록한다.
    if can:
        ans = min(cnt, ans)

print(ans if ans != 101 else -1)
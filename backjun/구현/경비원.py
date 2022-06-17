n, m = map(int, input().split())
store = []
answer = 0
road = ((n * 2)+(m * 2))
c = int(input())
for _ in range(c+1):
    direction , position = map(int, input().split())
    if direction == 1:
        store.append(position)
    elif direction == 4:
        store.append(n+position)
    elif direction == 2:
        store.append(n+m+abs(position-n))
    elif direction == 3:
        store.append(n+n+m+abs(position - m))

dong_pos = store.pop()
for s in store:
    tmp = abs(dong_pos - s)
    answer += min(tmp, road - tmp)
print(answer)

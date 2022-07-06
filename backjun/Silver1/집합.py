import sys
m = int(sys.stdin.readline())
answer = set()
for _ in range(m):
    data = sys.stdin.readline().split()
    if len(data) != 1:
        num = int(data[1])
    if data[0] == 'add':
        answer.add(int(data[1]))
    elif data[0] == 'remove':
        answer.discard(num)
    elif data[0] == 'check':
        if num in answer:
            print(1)
        else:
            print(0)
    elif data[0] == 'toggle':
        if num in answer:
            answer.discard(num)
        else:
            answer.add(num)
    elif data[0] == 'all':
        answer.clear()
        answer = set((list(range(1,21))))
    elif data[0] == 'empty':
        answer.clear()

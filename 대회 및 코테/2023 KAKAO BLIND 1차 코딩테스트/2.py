def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_stack, pickup_stack = [], []
    for i in range(n):
        if deliveries[i] != 0:
            deliver_stack.append(i)
        if pickups[i] != 0:
            pickup_stack.append(i)
    while deliver_stack or pickup_stack:
        flag = cap
        if len(deliver_stack) == 0 and len(pickup_stack) != 0:
            answer += (pickup_stack[-1] + 1) * 2
        elif len(deliver_stack) != 0 and len(pickup_stack) == 0:
            answer += (deliver_stack[-1] + 1) * 2
        elif deliver_stack[-1] >= pickup_stack[-1]:
            answer += (deliver_stack[-1] + 1) * 2
        else:
            answer += (pickup_stack[-1] + 1) * 2
        while deliver_stack and flag != 0:
            index = deliver_stack.pop()
            if deliveries[index] <= flag:
                flag -= deliveries[index]
                deliveries[index] = 0
            else:
                deliveries[index] -= flag
                flag = 0
                deliver_stack.append(index)
        flag = cap - flag
        while pickup_stack and flag != 0:
            index = pickup_stack.pop()
            if pickups[index] <= flag:
                flag -= pickups[index]
                pickups[index] = 0
            else:
                pickups[index] -= flag
                flag = 0
                pickup_stack.append(index)

    print(answer)
    return answer
solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0])
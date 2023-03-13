def solution(cards):
    answer = 0
    for x in cards:
        ch = [1] * len(cards)
        G1, des = 0, x
        while 1:
            if ch[des-1] == 1:
                ch[des-1] = 0
                G1 += 1
                des = cards[des-1]
            else: break
        arr = []
        for i in range(len(cards)):
            if ch[i] == 1:
                arr.append(cards[i])
        if not arr: break
        G2 = 0
        for y in arr:
            tmp2, des = 0,y
            while 1:
                if ch[des-1] == 1:
                    ch[des-1] = 0
                    tmp2 += 1
                    des = cards[des-1]
                else:
                    G2 = max(G2, tmp2)
                    break
        answer = max(answer,G1*G2)
    return answer

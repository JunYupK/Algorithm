def solution(storey):
    answer = 0
    while storey:
        tmp = storey % 10
        if tmp > 5:
            answer += (10 - tmp)
            storey += 10
        elif tmp < 5:
            answer += tmp
        else:
            if(storey // 10) % 10 > 4:
                storey += 10
            answer += tmp
        storey //= 10
    return answer
solution(2554)
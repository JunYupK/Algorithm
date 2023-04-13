def solution(elements):
    answer = 0
    elements = elements + elements
    flag = 0
    ans_set = set()
    while flag != len(elements)//2:
        flag += 1
        for i in range(len(elements)):
            slide = i + flag
            if slide >= len(elements):
                break
            ans_set.add(sum(elements[i:slide]))
    answer += len(ans_set)
    return answer
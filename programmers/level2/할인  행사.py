def solution(want, number, discount):
    answer = 0
    basket = {}
    for i, item in enumerate(want):
        basket[item] = number[i]
    start,end=  0, 9
    for i in range(len(discount)-9):
        tmp = {}
        for idx in range(start,end+1):
            if discount[idx] in tmp:
                tmp[discount[idx]] += 1
            else:
                tmp[discount[idx]] = 1
        flag = True
        for item in basket.keys():
            if item not in tmp:
                flag = False
                break
            elif basket[item] != tmp[item]:
                flag = False
                break
        if flag:
            answer += 1
        start += 1
        end += 1
    return answer
solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
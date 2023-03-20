from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    left_index, right_index = 0, 0
    for g in goal:
        flag = False

        for i in range(left_index, len(cards1)):
            if cards1[i] == g:
                left_index = i+1
                flag = True
                break
        for i in range(right_index, len(cards2)):
            if cards2[i] == g:
                right_index = i+1
                flag = True
                break
        if flag is False:
            return 'No'
    return 'Yes'
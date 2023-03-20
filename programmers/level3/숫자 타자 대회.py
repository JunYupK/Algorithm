from collections import deque
def solution(numbers):
    answer = 0
    num_dict = {'1' : (0,0), '2':(0,1), '3':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(2,0), '8':(2,1), '9':(2,2), '*':(3,0), '0':(3,1), '#':(3,2)}
    pad = [[0] * 3 for _ in range(4)]
    left, right = (1,0), (1,2)
    for num in numbers:
        next_position = num_dict[num]
        left_value = abs(next_position[0] - left[0]) + abs(next_position[1] - left[1]) + 1
        right_value = abs(next_position[0] - right[0]) + abs(next_position[1] - right[1]) + 1
        if left_value > right_value:
            answer += right_value
            right = next_position
        else:
            answer += left_value
            left = next_position
    print(answer)
    return answer
solution("1756")

# DP로 풀어야 함!
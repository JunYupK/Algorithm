# def solution(r1, r2):
#     answer = 0
#     r1 = (2 * r1) - 1
#     r2 = (2 * r2) - 1
#     r1_count = r1 * r1 + 4
#     r2_count = r2 * r2 + 4
#     answer = r2_count - r1_count + 4
#     print(r1_count , r2_count)
#     return answer
from math import floor,ceil,sqrt
def solution(r1, r2):
    answer = 0
    for x in range(1,r2+1):
        max_y = floor(sqrt(r2**2-x**2))
        min_y = 0 if x>r1 else ceil(sqrt(r1**2-x**2))
        answer += max_y-min_y+1
    
    return answer*4
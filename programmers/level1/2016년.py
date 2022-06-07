def solution(a, b):
    answer = ''
    day = ["FRI","SAT", "SUN", "MON", "TUE", "WED", "THU"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = 0
    for i in range(a-1):
        day_count += mon[i]
    day_count += b
    answer = day[day_count%7 - 1]
    return answer

solution(1,1)
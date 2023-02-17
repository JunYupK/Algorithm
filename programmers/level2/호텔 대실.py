def solution(book_time):
    time_stamp = [0] * 1440
    answer = 0
    min_time = []
    for start, end in book_time:
        s_hour, s_min = start.split(":")
        e_hour, e_min = end.split(":")
        min_time.append([int(s_hour)*60 + int(s_min) , int(e_hour) * 60 + int(e_min)])
    min_time.sort()
    for start, end in min_time:
        for i in range(start, end+10):
            time_stamp[i] += 1
    return max(time_stamp)

print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
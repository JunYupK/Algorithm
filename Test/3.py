from datetime import datetime
def dateToSeconds(date):
    year, month, day, hour,time_min,time_second = map(int, date.split(':'))
    year_to_day = year * 360
    month_to_day = month * 30
    total_day = day + month_to_day + year_to_day
    day_to_seconds = total_day * 86400
    result = hour * 3600 + time_min * 60 + time_second + day_to_seconds
    return result
def secondToDate(seconds):
    day = seconds // 86400
    second = seconds % 86400
    year = day // 360
    month = (day % 360) // 30
    day = (day % 360) % 30
    hour = second // 3600
    time_min = second % 3600 // 60
    time_second = second % 3600 % 60
    return str(year)+":"+str(month)+":" + str(day)+":" + str(hour)+":" + str(time_min)+":" + str(time_second)

def notYearToSeconds(date):
    day, hour,time_min,time_second = map(int, date.split(':'))
    total_day = day
    day_to_seconds = total_day * 86400
    result = hour * 3600 + time_min * 60 + time_second + day_to_seconds
    return result
def solution(s, times):
    day_to_day = 1
    store_range = 0
    current_time = dateToSeconds(s)
    for time in times:
        next_time = current_time + notYearToSeconds(time)
        current_date = secondToDate(current_time).split(':')
        next_date = secondToDate(next_time).split(':')
        if int(current_date[2]) + 1 > 30 and int(next_date[2]) == 1:
            if int(current_date[1]) + 1 == int(next_date[1]):
                day_to_day += 1
        elif int(current_date[2]) + 1 == int(next_date[2]):
            day_to_day += 1
        current_time = next_time
    # print(s , secondToDate(current_time))
    # print(day_to_day)
    range_time = current_time - dateToSeconds(s)
    # print(range_time//86400 , range_time% 86400)
    range_time -= 86400 - dateToSeconds(s) % 86400
    if range_time < 0:
        return [1, 1]
    range_time -= current_time % 86400
    if range_time < 0:
        if day_to_day == 2:
            return [1,2]
        else:
            return [0,2]
    store_range = 2 + range_time//86400
    if day_to_day == store_range:
        day_to_day = 1
    else:
        day_to_day = 0
    return [day_to_day , store_range]

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))
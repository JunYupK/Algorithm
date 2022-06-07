import sys
sys.setrecursionlimit(10000)
num = []
def cutting(times, target, line, cur_time):
    if len(num) != 0:
        if min(num) < cur_time:
            return
    result = line
    tmp_time = 0
    for i in range(len(times)):
        result -= (i+1)
        if result < 0:
            return
        result += (i+1) * 2
        tmp_time = times[i] + cur_time + tmp_time
        if result > target:
            return
        elif result < target:
            cutting(times, target, result, tmp_time)
        else:
            num.append(tmp_time)
            return
        print(result)

def solution(n, times):
    answer = 0
    cutting(times, n ,1, 0)
    answer = min(num)
    print(num)
    return answer

times = list(range(2,100))
solution(100,times)
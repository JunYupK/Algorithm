from bisect import bisect_left
def solution(n, times):
    answer = 0
    times.sort()
    index = len(times) - 1
    left = 1
    right = times[-1] * n
    while left <= right:
        mid = (left + right)//2
        sum = 0
        for t in times:
            sum += mid // t
            if sum >= n:
                break
        if sum >= n:
            answer = mid
            right = mid - 1
        elif sum < n:
            left = mid + 1
    return answer
# 이분탐색삘이다 싶으면 이분탐색을 하는 조건 기준을 다양하게 생각해보자, 주어진 리스트만으로 이분탐색을 하려고 하면 문제가 막막해진다!

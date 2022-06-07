def solution(nums):
    answer = 0
    n = len(nums)
    nums = set(nums)
    if n/2 >= len(nums):
        return len(nums)
    else:
        return n/2

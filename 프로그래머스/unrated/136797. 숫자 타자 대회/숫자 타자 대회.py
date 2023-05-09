from collections import defaultdict
import sys
import math
sys.setrecursionlimit(200000)
cache = defaultdict(dict)
W = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
]
def backtracking(depth, left, right,numbers):
    if depth == len(numbers):
        return 0
    if (left, right) in cache[depth]:
        return cache[depth][(left,right)]
    w = math.inf
    num = numbers[depth]
    if num != right:
        w = min(w,backtracking(depth + 1, num, right, numbers)+W[left][num])
    if num != left:
        w = min(w, backtracking(depth+1, left, num, numbers) + W[right][num])
    cache[depth][(left, right)] = w
    return w
def solution(numbers):
    answer = 0
    numbers = list(int(x) for x in numbers)
    
    return backtracking(0,4,6,numbers)
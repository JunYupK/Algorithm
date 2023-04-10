import sys
from itertools import permutations
def next_permutations(s):
    k = -1
    for i in range(len(s) - 1):
        if s[i] < s[i+1]:
            k = i
    if k == -1:
        return False
    for i in range(len(s)-1, -1, -1):
        if s[k] < s[i]:
            m = i
            break

    s[k], s[m] = s[m], s[k]
    L = s[:k+1]
    L.extend(list(reversed(s[k+1:])))
    return L
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    word = list(input().rstrip())
    answer = next_permutations(word)
    if answer:
        print(''.join(answer))
    else:
        print(''.join(word))


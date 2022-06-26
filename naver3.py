# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    # write your code in Python 3.6
    node = {}
    answer = 0
    tmp = N
    for i in range(len(A)):
        if A[i] not in node:
            node[A[i]] = 1
        else:
            node[A[i]] += 1
        if B[i] not in node:
            node[B[i]] = 1
        else:
            node[B[i]] += 1

    node = dict(sorted(node.items(), key=lambda x:x[1], reverse=True))
    for k, v in node.items():
        node[k] = tmp
        tmp -= 1
    for i in range(len(A)):
        answer += node[A[i]] + node[B[i]]
    return answer

A = [1]
B = [3]
N = 3
solution(N,A,B)
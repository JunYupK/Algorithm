from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]
def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)] , q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer

# trie 자료구조아니면 못푸는 줄 알았던 문제이다. 구글링에서도 대부분 trie를 사용하였지만 이진탐색으로도 풀리는 문제였다..
# 개수가 10000 이므로 2차원 배열로 선언후에 문자열의 길이별로 각 리스트에 담은 후 sort를 진행 하고 fro?? 가 들어오면 문자열의 길이가
# 5인 리스트에서 fro가 들어가는 문자의 개수를 이진탐색을 이용한 범위 개수 구하기로 구할 수 있다. 속도도 trie 에 비해 40배 가까이 빨랐다..
# 이진탐색을 이런 문자열에도 사용 할 수 있다는 것을 명심하자.
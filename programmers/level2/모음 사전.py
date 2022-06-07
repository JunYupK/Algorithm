def solution(word):
    answer = 0
    obj = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    plus = [781,156,31,6,1]
    for i in range(len(word)):
        for j in range(4, i, -1):
            answer += 5 ** (j - i) * obj[word[i]]
        answer += 1 + obj[word[i]]
    return answer
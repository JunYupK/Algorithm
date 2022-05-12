def solution(n, words):
    answer = []
    prev = ''
    overlap = {}
    human = {}
    for i in range(n):
        human[i] = 0
    for i in range(len(words)):
        human[(i % n)] += 1
        if i == 0:
            overlap[words[i]] = 0
            prev = words[0][-1]
            continue

        if prev != words[i][0] or overlap.get(words[i]) is not None:
            return [i%n + 1, human[(i % n)]]
        prev = words[i][-1]
        overlap[words[i]] = 0

    print(human)

    return [0,0]

words = ['qwe', 'eqwe', 'eqwe']
print(solution(2,words))
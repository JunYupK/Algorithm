from collections import Counter
def solution(X, Y):
    answer = ''
    x_counter = Counter(X)
    y_counter = Counter(Y)
    source = []
    for k,v in x_counter.items():
        if k in y_counter:
            count = min(x_counter[k], y_counter[k])
            for i in range(count):
                source.append(k)
    source.sort(reverse = True)
    if source:
        if source[0] == '0':
            return '0'
        else:
            return "".join(source)
    else:
        return "-1"
    return answer
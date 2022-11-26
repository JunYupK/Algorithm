def dateToInt(data):
    data = data.split(".")
    result = (int(data[0]) * 28 * 12) + (int(data[1]) * 28) + int(data[2])
    return result
def solution(today, terms, privacies):
    answer = []
    termDict = {}
    today = dateToInt(today)
    i = 1
    print(today)
    for term in terms:
        tmp = term.split(" ")
        termDict[tmp[0]] = int(tmp[1]) * 28
    for x in privacies:
        date, term = x.split(" ")
        result = dateToInt(date) + termDict[term]
        print(result)
        if today >= result:
            answer.append(i)
        i += 1
    print(answer)
    return answer



solution("2020.01.01",["Z 3", "D 5"],  ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
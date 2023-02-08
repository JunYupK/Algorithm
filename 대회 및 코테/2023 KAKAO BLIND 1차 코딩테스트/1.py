def solution(today, terms, privacies):
    answer = []
    promise = {}
    def yearToDay(date):
        date= date.split('.')
        year, month, day = date[0], date[1], date[2]
        return (int(year) * 12 * 28) + (int(month) * 28) + int(day)
    for term in terms:
        x, y = term.split(' ')
        promise[x] = int(y)
    today = yearToDay(today)
    for i in range(len(privacies)):
        tmpDay, tmpPro = privacies[i].split(' ')
        tmp = yearToDay(tmpDay) + promise[tmpPro] * 28
        if today >= tmp:
            answer.append(i+1)
    return answer
solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
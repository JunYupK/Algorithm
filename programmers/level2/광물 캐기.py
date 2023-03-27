def solution(picks, minerals):
    answer = 0
    minerals_mass = []
    count = sum(picks)
    set_count = 0
    tmp = [0, 0, 0]
    for i, m in enumerate(minerals):
        if set_count == count:
            break
        if m == 'diamond':
            tmp[0] += 1
        elif m == 'iron':
            tmp[1] += 1
        else:
            tmp[2] += 1

        if (i + 1) % 5 == 0:
            set_count += 1
            minerals_mass.append(tmp)
            tmp = [0, 0, 0]
    if len(tmp) != 0:
        if set_count < count:
            minerals_mass.append(tmp)
    minerals_mass.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    print(minerals_mass)
    for mass in minerals_mass:
        if picks[0] != 0:
            answer += sum(mass)
            picks[0] -= 1
        elif picks[1] != 0:
            answer += mass[0] * 5
            answer += mass[1] + mass[2]
            picks[1] -= 1
        elif picks[2] != 0:
            answer += mass[0] * 25
            answer += mass[1] * 5
            answer += mass[2]
            picks[2] -= 1
        else:
            return answer
    return answer
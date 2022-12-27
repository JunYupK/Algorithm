# Day에 2번사는 것 체크
# K 체크
def solution(id_list, k):
    answer = 0
    total_coupon = {}
    for i, id in enumerate(id_list):
        day_coupon = {}
        clients = id.split(' ')
        for c in clients:
            if c in day_coupon:
                continue
            else:
                day_coupon[c] = True
            if c in total_coupon and total_coupon[c]>k:
                continue
            elif c in total_coupon and total_coupon[c] < k:
                answer += 1
                total_coupon[c] += 1
            elif c not in total_coupon:
                answer += 1
                total_coupon[c] = 1
    return answer

print(solution(["A B C D", "A D", "A B D", "B D"],2))
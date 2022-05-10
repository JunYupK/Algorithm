def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2
    return answer

#2017문제라 딱히 구현이 어렵지도 않았다 가볍게 보고 넘어갈 문제라 생각한다.
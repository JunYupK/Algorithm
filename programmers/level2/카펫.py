def solution(brown, yellow):
    for width in range(1 , 2000000):
        for height in range(1 , width+1):
            if brown == (width + 2) * (height + 2) - (width * height) and width * height == yellow:
                return [width+2, height+2]
#전형적인 완전탐색 brute force 문제 다른 문제를 보니 공식이 있는것도 같지만 문제의 근본 목적이 완전탐색이기 때문에 완전탐색으로 풀었다.
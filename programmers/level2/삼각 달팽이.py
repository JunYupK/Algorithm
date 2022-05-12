from itertools import chain #2차원 배열을 1차원으로 만들어 주는 라이브러리
def solution(n):
    answer = []
    tri = []
    count = 1
    for i in range(n):
        tri.append([0]* (i+1) )
    height = len(tri)
    width = len(tri[-1])
    i_index = 0
    j_index = 0
    if n == 1:
        return [1]

    while height >= 1:
        for i in range(i_index ,i_index + height):
            tri[i][j_index] = count
            count += 1
        i_index = i
        j_index += 1
        for j in range(j_index,j_index + width -1):
            tri[i_index][j] = count
            count += 1
        j_index = j
        for _ in range(height-2):
            i_index -= 1
            j_index -= 1
            tri[i_index][j_index] = count
            count += 1
        i_index += 1
        height -= 3
        width -= 3
    answer = list(chain.from_iterable(tri)) #2차원 리스트를 1차원 리스트로 변환
    return answer
solution(1)

#배열형태로 찍었을때 나타나는 형태를 파악하고 구현에 신경쓰는 문제이다.

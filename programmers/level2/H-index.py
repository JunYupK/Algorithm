from bisect import bisect_left
def solution(citations):
    answer = []
    citations = sorted(citations, reverse= True)
    print(citations)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)

citations   = 	[0,0,0,0,0]
print(solution(citations))
#문제 설명이 너무 빈약하다 이해하기 너무 힘들었다
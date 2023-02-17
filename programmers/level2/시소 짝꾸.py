from collections import defaultdict
from itertools import product
def solution(weights):
    answer = 0
    distance = [1,2/3,1/2,3/4,3/2, 2, 4/3]
    humans = defaultdict(int)
    for w in weights:
        for d in distance:
            answer += humans[d * w]
        humans[w] += 1

    return answer

solution([100,180,360,100,270])


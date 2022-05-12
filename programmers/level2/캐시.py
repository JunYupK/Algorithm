from collections import deque
def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for k, city in enumerate(cities):
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5
    print(cache)
    print(time)
    return time
# deque 사이즈 조절하는데 가장 애먹었던 문제인데 maxlen이라는 자체적인 속성을 제공했었다 -.-
# heap의 경우에는 꽉 차있는데 체크를 안해주면 프로그램이 터졌는데. deque의 경우에는 꽉 차 있는 상황에서 append를 하면 무시를 해주는 것 같다...
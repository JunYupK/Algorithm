def solution(routes):
    answer = 0
    print(sorted(routes, key=lambda x:x[0]))
    routes = sorted(routes, key=lambda x:x[1])
    camera = 1
    end = routes[0][1]
    for i in range(1 , len(routes)):
        if routes[i][1] >= end >= routes[i][0]:
            continue
        else:
            camera += 1
            end = routes[i][1]

    print(camera)
    return camera


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)
def solution(participant, completion):
    answer = ''
    success = {}
    for name in participant:
        if success.get(name) is not None:
            success[name] += 1
        else:
            success[name] = 1
    for name in completion:
        success[name] -= 1
    for k, v in success.items():
        if v != 0:
            return k

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)
import api as kakaoAPI
from collections import deque

if __name__ == "__main__":
    res = kakaoAPI.startAPI(1)
    turn = 0
    auth_key, problem, time = res["auth_key"], res['problem'], res['time']
    kakaoAPI.scoreAPI(auth_key)
    # while turn <= 595:
    #     user_info = kakaoAPI.userInfoAPI(auth_key)['user_info']
    #     waiting_queue = deque(kakaoAPI.waitingLineAPI(auth_key)['waiting_line'])
    #     pairs = []
    #     while len(waiting_queue) >= 2:
    #         user1 = waiting_queue.popleft()['id']
    #         user2 = waiting_queue.popleft()['id']
    #         pairs.append([user1, user2])
    #     kakaoAPI.matchAPI(auth_key, pairs)
    #     kakaoAPI.gameResultAPI(auth_key)
    #     print(turn)
    #     turn += 1
    # kakaoAPI.scoreAPI(auth_key)

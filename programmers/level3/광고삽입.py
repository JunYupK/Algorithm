# import time
#
# def time_to_int(s):
#     tmp1 = s.split(':')
#     num = 3600 * int(tmp1[0]) + 60 * int(tmp1[1]) +  int(tmp1[2])
#     return num
# def solution(play_time, adv_time, logs):
#     play_time = time_to_int(play_time)
#     adv_time = time_to_int(adv_time)
#     timezone = [0] * (play_time + 1)
#     for log in logs:
#         tmp = log.split('-')
#         start = time_to_int(tmp[0])
#         end = time_to_int(tmp[1])
#         timezone[start] += 1
#         timezone[end] -= 1
#
#     for i in range(1, play_time):
#         timezone[i] = timezone[i] + timezone[i-1]
#     for i in range(1, play_time):
#         timezone[i] = timezone[i] + timezone[i-1]
#
#     most_view = -1
#     max_time = 0
#     for i in range(adv_time - 1 , play_time):
#         if i >= adv_time:
#             if most_view < timezone[i] - timezone[i - adv_time]:
#                 most_view = timezone[i] - timezone[i-adv_time]
#                 max_time = i-adv_time + 1
#
#         else:
#             if most_view < timezone[i]:
#                 most_view = timezone[i]
#                 max_time = i-adv_time + 1
#
#     most_time = time.strftime("%H:%M:%S", time.gmtime(max_time))
#     print(most_time)
#     return most_time
# play_time = "99:59:59"
# adv_time = 	"25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# solution(play_time, adv_time, logs)

#꼭 다시 풀어보기!!!!!
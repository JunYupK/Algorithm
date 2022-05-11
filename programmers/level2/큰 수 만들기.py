# def solution(number, k):
#     answer = []  # Stack
#
#     for num in number:
#         if not answer:
#             answer.append(num)
#             continue
#         if k > 0:
#             while answer[-1] < num:
#                 answer.pop()
#                 k -= 1
#                 if not answer or k <= 0:
#                     break
#         answer.append(num)
#
#     answer = answer[:-k] if k > 0 else answer
#     return ''.join(answer)
#
# #의외로 애 먹었던 문제다 결국 구글링으로 풀었다.
# # 스택을 사용하여 순차적으로 제일 큰수만을 남기면서 숫자를 만들어나가는 형식, 작은값이 생기면 pop을 하며 k 값을 줄여나가는 형식이다
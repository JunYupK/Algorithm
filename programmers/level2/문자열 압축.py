from collections import deque
def solution(s):
    answer = 0
    answer_list = []
    tmp = []
    cnt = 1
    while cnt != len(s):
        tmp = []
        count = 1
        for i in range(0,len(s), cnt):
            tmp.append(s[i:i+cnt])
        tmp_str = ""
        for i in range(1, len(tmp)):
            if tmp[i] == tmp[i-1]:
                count += 1
            else:
                if count == 1:
                    count = ""
                tmp_str += str(count) + tmp[i-1]
                count = 1

        if count == 1:
            count = ""
        tmp_str += str(count) + tmp[i]
        cnt += 1

        answer_list.append(len(tmp_str))

    if len(answer_list) == 0:
        answer = 1
    else:
        answer = min(answer_list)
    return answer

# 위에는 단순한 문자열 인덱싱을 이용한 방법이고 아래 코드는 새롭게 deque를 활용하여 스택을 활용한 중복문자 거르기 방법을 사용하여 풀어 봤다 아래쪽이 더 코드의 간결성과 가독성이 좋은것같다.

#******************************************************************************************************************************************************************************************************

from collections import deque


def solution(s):
    answer = []
    num = len(s) // 2
    if len(s) == 1:
        return 1
    for n in range(1, num + 1):
        st = deque()
        count = 0
        for i in range(0, len(s), n):
            tmp = s[i:i + n]
            if len(st) == 0:
                st.append(tmp)
                continue
            if tmp == st[-1]:
                count += 1
            else:
                if count == 0:
                    st.append(tmp)
                else:
                    st[-1] += str(count + 1)
                    count = 0
                    st.append(tmp)
        if count != 0:
            st[-1] += str(count + 1)
        answer.append(len("".join(list(st))))
    return min(answer)
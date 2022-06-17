from collections import deque
data = str(input())
st = deque()
answer = 0
tmp = 1
for i ,char in enumerate(data):
    if char == '(':
        st.append(char)
        tmp *= 2
    elif char == '[':
        st.append(char)
        tmp *= 3
    elif char == ')':
        if not st or st[-1] == '[':
            answer = 0
            break
        if data[i-1] == '(':
            answer += tmp
        st.pop()
        tmp = tmp// 2
    elif char == ']':
        if not st or st[-1] == '(':
            answer = 0
            break
        if data[i - 1] == '[':
            answer += tmp
        st.pop()
        tmp = tmp// 3

if st:
    print(0)
else:
    print(answer)
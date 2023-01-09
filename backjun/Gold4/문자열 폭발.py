import sys
s = input()
explosion = input()
answer = []
for char in s:
    answer.append(char)
    if "".join(answer[len(answer)- len(explosion): len(answer)]) == explosion:
        for _ in range(len(explosion)):
            answer.pop()

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))
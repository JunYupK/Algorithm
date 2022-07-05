from itertools import combinations
l , c = map(int,input().split())
data = list(input().split())

vowel_dic = {'a':True, 'e':True, 'o':True, 'i':True, 'u':True}
vowel = []
cons = []
answer = []
data.sort()
for char in data:
    if char in vowel_dic:
        vowel.append(char)
    else:
        cons.append(char)

for i in range(1, len(vowel)+1):
    if l - i < 2:
        break
    for c1 in combinations(vowel, i):
        for c2 in combinations(cons,l - i):
            tmp = list(c1+c2)
            tmp.sort()
            answer.append("".join(tmp))
answer = sorted(answer)
for d in answer:
    print(d)
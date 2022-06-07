from collections import deque, defaultdict
def solution(skill, skill_trees):
    answer = 0
    skill_dict = defaultdict(list)
    q = deque()
    for i in range(len(skill)):
        skill_dict[skill[i]] = list(skill[0:i])
    skill = list(skill)
    for word in skill_trees:
        check = True
        for char in word:
            if char in skill:
                for x in skill_dict[char]:
                    if x not in q:
                        check = False
                        break
            q.append(char)
        q.clear()
        if check is True:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill,skill_trees)
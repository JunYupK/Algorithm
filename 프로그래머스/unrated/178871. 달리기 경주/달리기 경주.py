def solution(players, callings):
    answer = []
    name_dict =  {}
    ranking_dict = {}
    for i, player in enumerate(players):
        name_dict[player] = i+1
        ranking_dict[i+1] = player
    
    for call in callings:
        tmp_ranking = name_dict[call]
        taken_name = ranking_dict[tmp_ranking-1]
        name_dict[call] = tmp_ranking - 1
        name_dict[taken_name] = tmp_ranking
        ranking_dict[tmp_ranking] = taken_name
        ranking_dict[tmp_ranking-1]= call
    for i in range(len(players)):
        answer.append(ranking_dict[i+1])
    return answer
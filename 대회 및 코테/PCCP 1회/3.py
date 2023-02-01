def recursion(depth, idx):
    if depth == 1:
        return "Rr"
    elif depth == 2:
        gen = ["RR", "Rr", "Rr", "rr"]
        return gen[idx]
    else: # depth >= 3
        total_idxs = 4**(depth-1)
        quarter_idxs = total_idxs // 4

        if idx < quarter_idxs:
            return "RR"
        elif idx < 3 * quarter_idxs:
            return recursion(depth-1, idx % quarter_idxs)
        else:
            return "rr"

def solution(queries):
    answer = []
    for depth, idx in queries:
        answer.append(recursion(depth, idx-1))

    return answer
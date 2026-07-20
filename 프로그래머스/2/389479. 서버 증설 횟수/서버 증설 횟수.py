def solution(players, m, k):
    answer = 0
    
    for idx in range(24):
        while players[idx] >= m:
            for _idx in range(idx, idx+k):
                if _idx > 23:
                    continue
                players[_idx] -= m
            answer += 1
    
    return answer
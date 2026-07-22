def solution(n, q, ans):
    answer = 0
    
    q = list(map(set, q))
    
    from itertools import combinations
    
    combs = combinations(list(range(1, n+1)), 5)
    
    for comb in combs:
        for code_idx in range(len(q)):
            if len(set(comb) & q[code_idx]) != ans[code_idx]:
                break
        else:
            answer += 1    
        
    return answer
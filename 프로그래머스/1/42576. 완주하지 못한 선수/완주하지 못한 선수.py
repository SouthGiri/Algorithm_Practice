def solution(participant, completion):
    
    from collections import Counter
    
    count = Counter(participant)
    
    for com in completion:
        count[com] -= 1
    
    count += Counter()
    
    answer = list(count)[0]
    return answer
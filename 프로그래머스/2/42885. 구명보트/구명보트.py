def solution(people, limit):
    from math import ceil
    
    answer = 0
    small, big = [], []
    
    for p in people:
        (small if p <= limit//2 else big).append(p)
    
    small.sort(reverse=True)
    big.sort()
    
    while small and big:
        if small[-1] + big[-1] <= limit:
            small.pop()
        
        big.pop()
        answer += 1
    
    answer += (ceil(len(small) / 2) + len(big))
    return answer
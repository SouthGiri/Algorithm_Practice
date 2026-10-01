def solution(citations): 
    answer = 0
    N = len(citations)
    left, right = 0, N
    
    citations.sort()
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid == 0 or citations[N-mid] >= mid:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    
    
    return answer
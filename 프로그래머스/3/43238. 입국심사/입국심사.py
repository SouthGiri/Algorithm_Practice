def solution(n, times):
    answer = int(1e18)
    left, right = 1, 1e18
    
    while left <= right:
        mid = (left + right) // 2
        res = 0
        for time in times:
            res += (mid // time)
        
        if res >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

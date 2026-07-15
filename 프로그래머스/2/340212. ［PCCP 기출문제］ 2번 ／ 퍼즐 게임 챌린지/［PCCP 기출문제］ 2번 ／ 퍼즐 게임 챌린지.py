def solution(diffs, times, limit):
    N = len(diffs)
    
    low = 1
    high = 9e9
    
    answer = 9e9
    
    while low < high:
        level = (low + high) // 2
        total_time = 0
        for i in range(N):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                total_time += ((diffs[i] - level) * (times[i] + times[i-1]) + times[i])
        
        if total_time > limit:
            
            low = level+1
        else:
            high = level
            answer = min(answer, level)

    return answer
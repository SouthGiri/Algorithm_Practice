def solution(operations):
    from heapq import heappush, heappop
    from collections import Counter
    
    
    max_h, min_h = [], []
    max_cnt, min_cnt = Counter(), Counter()
    
    for oper in operations:
        
        op, num = oper.split()
        num = int(num)
        if op == 'I':
            heappush(max_h, -num)
            heappush(min_h, num)
        
        elif op == 'D' and num == 1:
            while max_h and max_cnt[-max_h[0]] > 0:
                max_cnt[-heappop(max_h)] -= 1
            
            if max_h:
                val = -heappop(max_h)
                min_cnt[val] += 1
        
        else:
            while min_h and min_cnt[min_h[0]] > 0:
                min_cnt[heappop(min_h)] -= 1
            
            if min_h:
                val = heappop(min_h)
                max_cnt[val] += 1
    
    while max_h and max_cnt[-max_h[0]] > 0:
        max_cnt[-heappop(max_h)] -= 1
    
    while min_h and min_cnt[min_h[0]] > 0:
        min_cnt[heappop(min_h)] -= 1
    
    if max_h and min_h:
        ans = [-max_h[0], min_h[0]]
    else:
        ans = [0, 0]
        
    return ans
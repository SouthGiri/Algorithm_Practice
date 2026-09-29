def solution(operations):
    from heapq import heappush, heappop
    from collections import Counter
    
    
    max_h, min_h = [], []
    cnt = Counter()
    
    for oper in operations:
        
        op, num = oper.split()
        num = int(num)
        if op == 'I':
            heappush(max_h, -num)
            heappush(min_h, num)
            cnt[num] += 1
        
        elif op == 'D' and num == 1:
            while max_h and cnt[-max_h[0]] == 0:
                cnt[-heappop(max_h)] -= 1
            
            if max_h:
                cnt[-heappop(max_h)] -= 1
        
        else:
            while min_h and cnt[min_h[0]] == 0:
                cnt[heappop(min_h)] -= 1
            
            if min_h:
                cnt[heappop(min_h)] -= 1
        
    
    while max_h and cnt[-max_h[0]] == 0:
        heappop(max_h)
    
    while min_h and cnt[min_h[0]] == 0:
        heappop(min_h)
    
    if max_h and min_h:
        ans = [-max_h[0], min_h[0]]
    else:
        ans = [0, 0]
        
    return ans
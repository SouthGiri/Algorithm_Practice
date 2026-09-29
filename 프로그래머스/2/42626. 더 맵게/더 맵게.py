def solution(scoville, K):
    from heapq import heapify, heappop, heappush
    
    answer = 0
    h = scoville
    heapify(h)
    
    while h[0] < K:
        if len(h) == 1:
            return -1
        
        a = heappop(h)
        b = heappop(h)
        mixed = a + b*2
        heappush(h, mixed)
        answer += 1
        
    return answer
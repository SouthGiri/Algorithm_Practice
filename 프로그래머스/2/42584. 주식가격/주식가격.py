def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = []
    
    for idx in range(N):
        while stack and prices[stack[-1]] > prices[idx]:
            val = stack.pop()
            answer[val] = idx - val
        
        stack.append(idx)
        
    while stack:
        val = stack.pop()
        answer[val] = N - val - 1
    
    return answer
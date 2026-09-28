def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    
    for idx in range(N):
        while stack and numbers[idx] > numbers[stack[-1]]:
            val = stack.pop()
            answer[val] = numbers[idx]
        
        stack.append(idx)
    
    return answer
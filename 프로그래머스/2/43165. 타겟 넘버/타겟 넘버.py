def solution(numbers, target):
    N = len(numbers)
    
    def dfs(depth, total):
        if depth == N:
            return int(total == target)
        
        return dfs(depth + 1, total + numbers[depth]) + dfs(depth + 1, total - numbers[depth])
    
    answer = dfs(0, 0)
    
    return answer
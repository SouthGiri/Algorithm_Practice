def solution(numbers, target):
    N = len(numbers)
    answer = 0
    
    numbers.sort(reverse=True)
    
    def dfs(depth, tmp):
        nonlocal answer

        if depth == N:
            if tmp == target:
                answer += 1
            return

        if tmp < 0 and sum(numbers[depth:]) <= abs(tmp):
            return

        dfs(depth + 1, tmp + numbers[depth])
        dfs(depth + 1, tmp - numbers[depth])
    
    dfs(0, 0)
    
    return answer
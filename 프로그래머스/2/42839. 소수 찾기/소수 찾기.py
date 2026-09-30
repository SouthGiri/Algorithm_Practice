def solution(numbers):

    M = len(numbers)
    used = [False] * M
    comb = set()
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def dfs(depth, num):
        if depth == M+1:
            return
        
        if depth > 0:
            comb.add(int(num))
        
        for idx, next_num in enumerate(numbers):
            if not used[idx]:
                used[idx] = True
                dfs(depth+1, num+next_num)
                used[idx] = False
    
    dfs(0, '')
    
    comb -= {0, 1}
    answer = sum(is_prime(c) for c in comb)
        
    return answer
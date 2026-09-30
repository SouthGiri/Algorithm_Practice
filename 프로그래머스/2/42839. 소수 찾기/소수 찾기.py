def solution(numbers):
    N = 10_000_000
    is_prime = [True] * N
    M = len(numbers)
    used = [False] * M
    
    for i in range(2, int(N**0.5)):
        if is_prime[i]:
            j = 2
            while i*j < N:
                is_prime[i*j] = False
                j += 1
    
    comb = set()
    
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
    answer = sum(is_prime[c] for c in comb)
        
    return answer
def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0] * N for _ in range(N)]
    
    dp[0][0] = triangle[0][0]
    
    for r in range(N):
        for c in range(r+1):
            dp[r][c] = triangle[r][c] + max(dp[r-1][c-1], dp[r-1][c])
    
    answer = max(dp[r])
    return answer
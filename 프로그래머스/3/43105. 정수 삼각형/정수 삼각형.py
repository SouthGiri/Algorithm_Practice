def solution(triangle):
    N = len(triangle)
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = triangle[0][0]
    
    for row in triangle[1:]:
        idx = len(row)-1
        for col in range(len(row)):
            dp[idx][col] = triangle[idx][col] + max(dp[idx-1][col-1], dp[idx-1][col])
    
    return max(dp[-1])
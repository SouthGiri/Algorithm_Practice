import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, c):
    if (r, c) == (M-1, N-1):
        return 1
    
    # not visited -> calc dp value recursively
    if dp[r][c] == -1:
        dp[r][c] = 0        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] < graph[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]


dr, dc = (0, 0, -1, 1), (-1, 1, 0, 0)
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))
import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
d = [0] * (N+1)
dp = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0

for i in range(N):
    a, b = map(int, input().split())
    d[i] = a
    if i == N-1:
        d[i+1] = b

for level in range(1, N):
    for i in range(1, N):
        j = i+level
        if j <= N:
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j])

print(dp[1][N])
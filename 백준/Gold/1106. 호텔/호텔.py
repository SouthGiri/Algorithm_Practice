import sys
input = sys.stdin.readline

import math

C, N = map(int, input().split())
ads = [0]
for _ in range(N):
    cost, customer = map(int, input().split())
    ads.append((cost, customer))

ans = 0
dp = [[0] * (C+1) for _ in range(N+1)]

for i in range(1, C+1):
    dp[1][i] = math.ceil(i/ads[1][1]) * ads[1][0]

for i in range(2, N+1):
    for j in range(1, C+1):
        cost, customer = ads[i]
        if j >= customer:
            dp[i][j] = min(dp[i-1][j], dp[i][j-customer] + cost)
        else:
            dp[i][j] = min(dp[i-1][j], cost)
print(dp[N][C])
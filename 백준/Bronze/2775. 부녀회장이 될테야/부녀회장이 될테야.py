import sys
input = sys.stdin.readline

t = int(input())
dp = [[0] * 15 for _ in range(15)]

for i in range(15):
    dp[0][i] = i+1
    dp[i][0] = 1


for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])

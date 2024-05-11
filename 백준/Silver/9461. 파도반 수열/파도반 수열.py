import sys
input = sys.stdin.readline

t = int(input())

dp = [0, 1, 1, 1]
for _ in range(t):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append(dp[i-2] + dp[i-3])
    print(dp[n])
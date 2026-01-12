import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort()

dp = [0] * (K+1)

for i in range(0, K+1, coins[0]):
    dp[i] = 1

for coin in coins[1:]:
    for val in range(coin, K+1):
        dp[val] += dp[val-coin]

print(dp[K])
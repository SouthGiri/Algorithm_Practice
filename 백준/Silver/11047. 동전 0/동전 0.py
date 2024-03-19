import sys
input = sys.stdin.readline

# n종류 동전 -> 합 k 구할 때 동전의 최솟값
# k 보다 작으면서 가장 큰 동전부터 greedy
coins = []
answer = 0

n, k = map(int, input().split())
for _ in range(n):
    now = int(input())
    if now <= k:
        coins.append(now)

coins.sort(reverse=True)

for coin in coins:
    cnt = k // coin
    k %= coin
    answer += cnt

print(answer)
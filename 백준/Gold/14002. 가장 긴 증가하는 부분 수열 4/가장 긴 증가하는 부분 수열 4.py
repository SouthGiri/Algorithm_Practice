import sys
input = sys.stdin.readline


N = int(input())
data = list(map(int, input().split()))

dp = [1] * N

for j in range(1, N):
    for i in range(j):
        if data[i] < data[j]:
            dp[j] = max(dp[j], dp[i] + 1)

ans = length = max(dp)
res = []

for idx in range(N-1, -1, -1):
    if dp[idx] == length:
        res.append(data[idx])
        length -= 1


print(ans)
print(*res[::-1])
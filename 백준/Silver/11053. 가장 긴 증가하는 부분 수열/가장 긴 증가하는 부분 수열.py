import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp 이전 인덱스 전부랑 비교해서 현재 값이 해당 인덱스값보다 큰 경우의 최대
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    candi = []
    for j in range(0, i):
        if a[i] > a[j]:
            candi.append(dp[j])
    if len(candi) != 0:
        dp[i] = max(candi) + 1
    else:
        dp[i] = 1

print(max(dp))
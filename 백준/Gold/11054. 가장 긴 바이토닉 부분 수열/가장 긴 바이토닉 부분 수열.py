import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

rev_a = a[::-1]

inc_dp = [1]*n
dec_dp = [1]*n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j]+1)

        if rev_a[i] > rev_a[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j]+1)

dec_dp = dec_dp[::-1]

res = []
for i in range(n):
    res.append(dec_dp[i] + inc_dp[i] - 1)

print(max(res))
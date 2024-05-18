import sys
input = sys.stdin.readline

# 1 -> 1
# 2 -> 11 -- ㅁ 3
# 3 -> 111 1-- --1 ㅁ1 1ㅁ 5
# 4 -> 1111 11-- 1--1 --11 11ㅁ 1ㅁ1 ㅁ11 ---- ㅁㅁ  --ㅁㅁ ㅁㅁ-- 11

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007

print(dp[n])
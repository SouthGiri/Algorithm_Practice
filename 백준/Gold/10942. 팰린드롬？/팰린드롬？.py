import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for start in range(N-i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif A[start] == A[end]:
            if start+1 == end:
                dp[start][end] = 1
            else:
                dp[start][end] = dp[start+1][end-1]

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
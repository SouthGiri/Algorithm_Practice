import sys
input = sys.stdin.readline

def matmul(A, B):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += A[i][k] * B[k][j]
            C[i][j] = tmp % 1000
    return C

def solution(n):
    if n <= 1:
        return A
    if not n in dp:
        dp[n] = matmul(solution(n//2), solution(n - n//2))
    return dp[n]

N, B = map(int, input().split())
A = []
for i in range(N):
    li = list(map(int, input().split()))
    for j in range(N):
        li[j] %= 1000
    A.append(li)
dp = {}
dp[1] = A

ans = solution(B)
for a in ans:
    print(*a)
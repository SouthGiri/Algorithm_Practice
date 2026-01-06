import sys
input = sys.stdin.readline

def hanoi(n, src, dst):
    if n == 0:
        return
    
    tmp = 6 - src - dst
    hanoi(n-1, src, tmp)
    print(src, dst)
    hanoi(n-1, tmp, dst)


N = int(input())
dp = [0] * 101
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + 2**(i-1)

print(dp[N])

if N <= 20:
    hanoi(N, 1, 3)
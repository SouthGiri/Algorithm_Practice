import sys
input = sys.stdin.readline

def max_power(x):
    a = 1
    while a <= x:
        a *= 2
    
    return a//2

N, K = map(int, input().split())

flag = False

if N <= K:
    ans = 0
else:
    for _ in range(K-1):
        
        x = max_power(N)
        if N == x:
            break

        N %= x
        
    x = max_power(N)
    if x == N:
        ans = 0
    else:
        ans = x - (N%x)

print(ans)
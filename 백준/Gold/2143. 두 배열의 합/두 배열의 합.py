import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

c = Counter()
ans = 0

for i in range(N):
    for j in range(i+1, N+1):
        val = sum(A[i:j])
        c[val] += 1

for i in range(M):
    for j in range(i+1, M+1):
        val = sum(B[i:j])
        if c[T - val] > 0:
            ans += c[T - val]

print(ans)
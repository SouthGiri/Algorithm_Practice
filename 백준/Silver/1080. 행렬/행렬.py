import sys
input = sys.stdin.readline

def flip(i, j):
    for di in range(3):
        for dj in range(3):
            A[i+di][j+dj] ^= 1

N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            ans += 1

if A == B:
    print(ans)
else:
    print(-1)
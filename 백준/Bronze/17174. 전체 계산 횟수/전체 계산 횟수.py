import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = n
while n:
    n = n // m
    ans += n
print(ans)
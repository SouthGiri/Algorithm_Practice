import sys
input = sys.stdin.readline

ans = 0
res = 0
for _ in range(4):
    out, ride = map(int, input().split())
    ans = ans - out + ride
    res = max(res, ans)

print(res)
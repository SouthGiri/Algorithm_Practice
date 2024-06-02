import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = []

for _ in range(m):
    p.append(int(input()))

p.sort()
ans = 0
cnt = 0

if n >= m:
    for i in range(m):
        value = p[i] * (m-i)
        if value > ans:
            ans = value
            cnt = p[i]
else:
    p = p[(m-n):]
    for i in range(n):
        value = p[i] * (n-i)
        if value > ans:
            ans = value
            cnt = p[i]

print(cnt, ans)
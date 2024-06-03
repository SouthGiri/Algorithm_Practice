import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = []

for _ in range(m):
    p.append(int(input()))

p.sort()
ans = 0
cnt = 0

for i in range(m):
    egg = min(m-i, n)

    if ans < egg * p[i]:
        ans = egg * p[i]
        cnt = p[i]

print(cnt, ans)
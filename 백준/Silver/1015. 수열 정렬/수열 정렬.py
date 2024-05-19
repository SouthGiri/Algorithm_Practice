import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

sa = sorted(a, reverse=False)

p = []
for i in range(n):
    p.append(sa.index(a[i]))
    sa[sa.index(a[i])] = -1

for i in range(n):
    print(str(p[i]), end=' ')
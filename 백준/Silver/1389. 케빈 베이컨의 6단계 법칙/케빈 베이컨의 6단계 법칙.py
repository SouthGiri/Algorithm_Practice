import sys
input = sys.stdin.readline

# floyd
from math import inf

n, m = map(int, input().split())
dist = [[inf] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    s, e = map(int, input().split())
    dist[s-1][e-1] = 1
    dist[e-1][s-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
res = []
for i in range(n):
    res.append(sum(dist[i]))

print(res.index(min(res))+1)
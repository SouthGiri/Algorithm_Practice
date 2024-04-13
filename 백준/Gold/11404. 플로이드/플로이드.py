import sys
input = sys.stdin.readline

# floyd
from math import inf

n = int(input())
m = int(input())
dist = [[inf] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c) 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j], end=' ') if dist[i][j] != inf else print(0, end=' ')
    print()
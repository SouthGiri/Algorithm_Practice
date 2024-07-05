import sys
input = sys.stdin.readline

from math import inf
from itertools import combinations
ans = inf
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1, j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1, j+1))

for chi in combinations(chicken, m):
    tmp = 0
    for h in house:
        chi_len = inf
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-chi[j][0]) + abs(h[1]-chi[j][1]))
        tmp += chi_len
    ans = min(ans, tmp)

print(ans)
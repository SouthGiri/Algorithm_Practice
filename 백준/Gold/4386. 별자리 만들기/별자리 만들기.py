import sys
input = sys.stdin.readline

from itertools import combinations

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
distances = []
for i in range(1, N+1):
    x, y = map(float, input().split())
    graph[i].append((x, y))

for idx_a, idx_b in combinations(range(1, N+1), 2):
    star_a = graph[idx_a][0]
    star_b = graph[idx_b][0]
    dist = abs(((star_a[0] - star_b[0])**2 + (star_a[1] - star_b[1])**2) ** 0.5)
    distances.append((dist, idx_a, idx_b))

distances.sort()

edge_cnt = 0
ans = 0
for dist, star_a, star_b in distances:
    if find(star_a) != find(star_b):
        union(star_a, star_b)
        ans += dist
        edge_cnt += 1
    
    if edge_cnt == N-1:
        break

print(round(ans, 2))
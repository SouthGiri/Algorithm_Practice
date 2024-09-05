import sys
input = sys.stdin.readline


n, m = map(int, input().split())

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

edges = []
parent = list(range(n+1))
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x : x[2])

ans = 0
last = 0
for a,b,c in edges:
    if find_set(a) != find_set(b):
        union(a,b)
        ans += c
        last = c
print(ans - last)
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
parent = [i for i in range(N)]
xarr, yarr, zarr = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    xarr.append((x, i))
    yarr.append((y, i))
    zarr.append((z, i))

xarr.sort()
yarr.sort()
zarr.sort()

edges = []
for idx in range(N-1):
    edges.append((abs(xarr[idx][0] - xarr[idx+1][0]), xarr[idx][1], xarr[idx+1][1]))
    edges.append((abs(yarr[idx][0] - yarr[idx+1][0]), yarr[idx][1], yarr[idx+1][1]))
    edges.append((abs(zarr[idx][0] - zarr[idx+1][0]), zarr[idx][1], zarr[idx+1][1]))

edges.sort()
ans = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)
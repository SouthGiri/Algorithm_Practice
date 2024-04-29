import sys
input = sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx, dy, dz = [0, 0, 0, 0, 1, -1], [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0]

def bfs(q):
    day = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                day = max(day, graph[nx][ny][nz])
                q.append((nx, ny, nz))
    return day

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))

day = bfs(q)

fail = False
for g in graph:
    for f in g:
        if 0 in f:
            fail = True

if fail:
    print(-1)
else:
    print(day - 1)
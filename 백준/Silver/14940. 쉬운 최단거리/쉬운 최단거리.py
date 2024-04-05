import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append([i,j])

    dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                if mat[nx][ny] == 0:
                    dist[nx][ny] = 0
                elif mat[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if mat[i][j] == 2 and dist[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
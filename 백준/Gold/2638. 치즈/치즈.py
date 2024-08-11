import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

dx, dy = [1,-1,0,0], [0,0,-1,1]

def bfs():
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

def melt():
    melted = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                melted += 1
            elif graph[i][j] >= 2:
                graph[i][j] = 1
    return melted

time = 0
while True:
    bfs()
    melted = melt()

    if melted:
        time += 1
    else:
        print(time)
        break